import json
import sys
import re
from utils.alfred import *
from utils.strings import *
from utils.input_output import *
from utils.pr import *

def pr_handler(link):
    pr_links = []

    pr_num = get_pr_number(link)
    wiki_link = '[{0} {1}]'. format(get_url_from_number(pr_num), 'PR {}'.format(pr_num))
    if pr_num:
        pr_url = get_url_from_number(pr_num)
        pr_links = (
            {
                "title": pr_url,
                "subtitle": "url",
                "arg": pr_url
            },
            {
                "title": wiki_link,
                "subtitle": "wiki link",
                "arg": wiki_link
            }
    )

    return pr_links

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

LINK_HANDLERS = [
    pr_handler
]

# print(json.dumps(alfred_list, indent=4))
link = get_single_user_input()
list_items = process_handlers(link, LINK_HANDLERS)
alfred_list = compose_alfred_list(list_items, item_composer)
print(json.dumps(alfred_list))
