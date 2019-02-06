import json
import sys
import re
from datetime import datetime, timedelta
from utils.date_time import *
from alfread import *

CITIES = {
    "shanghai": {
        "timezone": 8,
        "abbr": "SH"
    },
    "palo alto": {
        "timezone": -8,
        "abbr": "PA"
    }
}
PA_SH_HOUR_DELTA = 16
# TIME_FORMAT = "%H:%M:%S"
TIME_FORMAT = "%b/%d %H:%M"
HOURS_AHEAD = -4
HOURS_FORWARD = 20
CURRENT_CITY = 'shanghai'
DEFAULT_TARGET_CITY = 'palo alto'

def get_target_city():
    target_city = DEFAULT_TARGET_CITY

    if len(sys.argv) >= 2:
        city_start_str = sys.argv[1]

        found_city = False
        city_found = DEFAULT_TARGET_CITY
        for c in CITIES.keys():
            if c.startswith(city_start_str.lower()):
                city_found = c
                found_city = True
        
        if city_found:
            target_city = city_found
    
    return target_city

def get_timezone_list(current_time, target_city):
    # current_time = get_current_time(TIME_FORMAT)
    tz_list = [] # list of tuples [SH_TIME, PA_TIME, is_current]
    target_city_data = CITIES.get(target_city, 'palo alto')
    target_city_tz = target_city_data.get('timezone', 8)
    current_city_data = CITIES['shanghai']
    current_city_tz = current_city_data.get('timezone', 8)
    timezone_delta = current_city_tz - target_city_tz
    
    for hour_delta in range(HOURS_AHEAD, HOURS_FORWARD):
        # print('hour_delta', hour_delta)
        # city_hour_delta = 
        delta = timedelta(hours=hour_delta)
        current_city_time = current_time + delta
        target_city_time = current_city_time - timedelta(hours=timezone_delta)
        is_current = True if hour_delta == 0 else False

        item = (current_city_time, target_city_time, target_city, is_current)
        # print('item: ', item)
        tz_list.append(item)


    return tz_list

def compose_alfred_item(item_type, title, subtitle, arg, icon_path):
    return {
        "type": item_type,
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "icon": {
            "path": icon_path
        }
    }

def compose_alfred_list(time_list):
    results = {
            "items": []
    }

    for t in time_list:
        current_city_time, target_city_time, city, is_current = t
        cur_time_str = convert_time_by_format(TIME_FORMAT, current_city_time)
        tar_time_str = convert_time_by_format(TIME_FORMAT, target_city_time)
        is_current_str = '*' if is_current else ''
        cur_city_abbr = CITIES[CURRENT_CITY]['abbr']
        tar_city_abbr = CITIES[city]['abbr']

        title = '{0} {1} - {2} {3} {4}'.format(cur_city_abbr, cur_time_str, tar_city_abbr, tar_time_str, is_current_str)
        # subtitle = 'Current' if is_current else ''
        subtitle = ''

        item = compose_alfred_item('file', title, subtitle, '', '')
        results['items'].append(item)
    
    return results

# print('city:', target_city)
target_city =  get_target_city()
time_list = get_timezone_list(datetime.now(), target_city)
alfred_list = compose_alfred_list(time_list)


# print(json.dumps(alfred_list, indent=4))
print(json.dumps(alfred_list))
