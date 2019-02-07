import json
import sys
import re
from datetime import datetime, timedelta

# refer to https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
def format_time_to_obj(time_str):
    ''' Format time to datatime object '''
    try:
        return datetime.strptime(time_str, '%Y-%m-%d %H:%M')
    except:
        return None

def get_current_time(format):
    ''' get current time string in format '''

    return convert_time_by_format(format, datetime.now())

def convert_time_by_format(format, time_obj):
    ''' format datetime obbject to string according to format specified '''
    try:
        return datetime.strftime(time_obj, format)
    except:
        return None