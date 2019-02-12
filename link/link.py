import json
import sys
import re
from utils.alfred import *
from utils.strings import *
from utils.input_output import *
from utils.pr import *
from utils.nfs import *
from utils.confluence import *
import subprocess

def process_handlers(link, handlers):
    items = []
    for handler in handlers:
        items.extend(handler(link))

    return items

def item_composer(item):
    return compose_alfred_item(
        item.get('type', 'file'),
        item.get('title', 'title'),
        item.get('subtitle', 'subtitle'),
        item.get('arg', 'arg'),
        item.get('icon', "icon.png")
    )

#pass in an anchor <a href="protocol://url/to/thing">Name</a>
LINK_HANDLERS = [
    pr_handler,
    nfs_handler,
    confluence_handler
]

# print(json.dumps(alfred_list, indent=4))
link = get_single_user_input()
list_items = process_handlers(link, LINK_HANDLERS)
alfred_list = compose_alfred_list(list_items, item_composer)
print(json.dumps(alfred_list))
