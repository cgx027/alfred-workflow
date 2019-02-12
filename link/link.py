import json
import sys
import re
from utils.alfred import *
from utils.strings import *
from utils.input_output import *
from utils.pr import *
import subprocess

def pr_handler(link):
    pr_links = ()

    pr_num, comment_num = get_pr_number(link)
    if pr_num:
        pr_url = get_url_from_number(pr_num, comment_num)
        if comment_num:
            wiki_link = '[{0} PR {1}#{2}]'.format(pr_url, pr_num, comment_num)
            short_desc = 'PR {0}#c{1}'.format(pr_num, comment_num)
        else:
            wiki_link = '[{0} PR {1}]'.format(pr_url, pr_num)
            short_desc = 'PR {0}'.format(pr_num)
        pr_links = (
            {
                "title": pr_url,
                "subtitle": "full url",
                "arg": pr_url
            },
            {
                "title": wiki_link,
                "subtitle": "wiki link",
                "arg": wiki_link
            },
            {
                "title": short_desc,
                "subtitle": "short description",
                "arg": short_desc
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

#pass in an anchor <a href="protocol://url/to/thing">Name</a>
LINK_HANDLERS = [
    pr_handler
]

# print(json.dumps(alfred_list, indent=4))
link = get_single_user_input()
list_items = process_handlers(link, LINK_HANDLERS)
alfred_list = compose_alfred_list(list_items, item_composer)
print(json.dumps(alfred_list))
