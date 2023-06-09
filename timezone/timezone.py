import json
import sys
import re
import pytz
from typing import List
from dataclasses import dataclass
from datetime import datetime, timedelta
from utils.date_time import *
from utils.alfred import *

@dataclass
class CityTime:
    city: str
    time: datetime

@dataclass
class TimeItem:
    current_city: CityTime
    target_cities: List[CityTime]
    is_current: bool

CITIES = {
    "shanghai": {
        "timezone": 8,
        "abbr": "SH",
        "pst_enabled": False
    },
    "palo alto": {
        # "timezone": -8, # winter time
        "timezone": -7, # summer time
        "abbr": "PA",
        "pst_enabled": True
    },
    "bangalore": {
        "timezone": 5.5,
        "abbr": "BLR",
        "pst_enabled": False
    }
}
# PA_SH_HOUR_DELTA = 16
TIME_FORMAT = "%b/%d %H:%M"
HOURS_AHEAD = -4
HOURS_FORWARD = 20
CURRENT_CITY = 'shanghai'
DEFAULT_TARGET_CITIES = ['palo alto', 'bangalore']

def get_target_cities():
    target_cities = []

    if len(sys.argv) >= 2:
        city_start_str = sys.argv[1]
        if city_start_str:
            for c in CITIES.keys():
                if c.startswith(city_start_str.lower()):
                    target_cities.append(c)

    if not target_cities:
        # target_cities = DEFAULT_TARGET_CITIES
        target_cities = copy.copy(DEFAULT_TARGET_CITIES)

    # print('target_cities', target_cities)
    return target_cities

def is_pst_time():
    us_tz = pytz.timezone('US/Pacific')
    
    # print("tzname: ", us_tz.localize(datetime.now()).tzname())
    return us_tz.localize(datetime.now()).tzname() == 'PST'

def get_timezone_list(current_time, target_cities: list[str]) -> List[TimeItem]:
    # current_time = get_current_time(TIME_FORMAT)
    tz_list: List[TimeItem] = [] # list of tuples [SH_TIME, CITIES..., is_current]

    current_city_data = CITIES['shanghai']
    current_city_tz = current_city_data.get('timezone', 8)
    
    is_now_pst_time = is_pst_time()

    # print("is_pst_summer_time", is_pst_time())

    for hour_delta in range(HOURS_AHEAD, HOURS_FORWARD):
        target_cities_time: List[CityTime] = []

        for target_city in target_cities:
            target_city_data = CITIES.get(target_city, {})
            if not target_city_data:
                continue

            target_city_tz = target_city_data.get('timezone', 8)
            pst_enabled = target_city_data.get('pst_enabled', False)
            if pst_enabled and is_now_pst_time:
                target_city_tz -= 1

            timezone_delta = current_city_tz - target_city_tz

            # print('hour_delta', hour_delta)
            delta = timedelta(hours=hour_delta)
            current_city_time = current_time + delta
            current_city_time_obj = CityTime('shanghai', current_city_time)

            target_city_time = current_city_time - timedelta(hours=timezone_delta)

            target_cities_time.append(CityTime(target_city, target_city_time))

        is_current = True if hour_delta == 0 else False
        tz_list.append(TimeItem(current_city_time_obj, target_cities_time, is_current))

    return tz_list

def format_alfred_item(item: TimeItem):
    cur_time_str = convert_time_by_format(TIME_FORMAT, item.current_city.time)
    cur_city_abbr = CITIES[item.current_city.city]['abbr']
    is_current_str = '*' if item.is_current else ''

    target_city_str = ""
    for city in item.target_cities:
        abbr = CITIES[city.city]['abbr']
        target_city_str += f"{abbr} {convert_time_by_format(TIME_FORMAT, city.time)} "

    title = '{0} {1} - {2} {3}'.format(cur_city_abbr, cur_time_str, target_city_str, is_current_str)
    # subtitle = 'Current' if is_current else ''
    subtitle = ''

    item = compose_alfred_item('file', title, subtitle, '', '')
    return item

# print('city:', target_city)
target_city =  get_target_cities()
time_list = get_timezone_list(datetime.now(), target_city)
alfred_list = compose_alfred_list(time_list, format_alfred_item)

print(json.dumps(alfred_list, indent=4))
# print(json.dumps(alfred_list))
