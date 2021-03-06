#!/usr/bin/env python
import copy

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

def compose_alfred_list(item_list, item_handler):
    results = {
            "items": []
    }

    for item in item_list:
        results['items'].append(item_handler(item))
    
    return results

def append_to_alfred_list(alfred_list, items):
    if not alfred_list: 
        alfred_result = {
                "items": []
        }
    else:
        alfred_result = copy.deepcopy(alfred_list)

    alfred_result['items'].extend(items)
    
    return alfred_result
