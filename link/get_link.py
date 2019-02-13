import json
import sys
import re
from utils.alfred import *
from utils.strings import *
from utils.input_output import get_single_user_input, get_user_input_count
from utils.pr import *
from utils.nfs import *
from utils.confluence import *
from utils.wiki import *
from link.default import *

def process_handlers(link, text, handlers):
    items = []
    for handler in handlers:
        items.extend(handler(link, text))

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
    confluence_handler,
    wiki_handler,
    default_handler
]

def run(query=''):
    link = get_single_user_input(query=query, index=1)
    text = get_single_user_input(query=query, index=2)
    list_items = process_handlers(link, text, LINK_HANDLERS)
    alfred_list = compose_alfred_list(list_items, item_composer)
    print(json.dumps(alfred_list))
    return alfred_list

if __name__ == '__main__':
    run()
