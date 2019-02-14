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
    default_links = []

    if text:
        page_wiki_link = '[{0} {1}]'.format(link, text)
        link_with_user_text = link + ' ' + text if text else link

        default_links.extend([ 
            {
                "title": link_with_user_text,
                "subtitle": "default page url",
                "arg": link_with_user_text
            },
            {
                "title": page_wiki_link,
                "subtitle": "default page wiki txt",
                "arg": page_wiki_link
            },
        ])

    url_base = os.path.basename(link)
    if url_base:
        page_wiki_link = '[{0} {1}]'.format(link, url_base)
        link_with_user_text = link + ' ' + url_base

        default_links.extend([
            {
                "title": link_with_user_text,
                "subtitle": "default page url with base name",
                "arg": link_with_user_text
            },
            {
                "title": page_wiki_link,
                "subtitle": "default page wiki txt with base name",
                "arg": page_wiki_link
            },
            {
                "title": url_base,
                "subtitle": "default page base name",
                "arg": url_base
            },
        ])
    
    return default_links
