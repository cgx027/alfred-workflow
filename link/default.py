import os
import re
from utils.input_output import *
try:
    from urllib.parse import unquote
except:
    from urllib import unquote

def get_text_from_user_input(query=''):
    # the second user input should be the text for hyper link
    return get_single_user_input(query, 2)

def default_handler(link, text):
    default_links = ()

    if text:
        page_wiki_link = '[{0} {1}]'.format(link, text)

        default_links = (
            {
                "title": link,
                "subtitle": "page url",
                "arg": link
            },
            {
                "title": page_wiki_link,
                "subtitle": "page wiki txt",
                "arg": page_wiki_link
            },
        )
    
    return default_links
