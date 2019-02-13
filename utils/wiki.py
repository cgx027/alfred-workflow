import os
import re
try:
    from urllib.parse import unquote
except:
    from urllib import unquote
from .strings import extractByRegex

# https://wiki.eng.vmware.com/VSANCertification
# https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo
WIKI_HTTP_PREFIX = 'https://wiki.eng.vmware.com/'

def get_wiki_page(text):
    if not text.startswith(WIKI_HTTP_PREFIX):
        return None
    text_decoded = unquote(text)
    return os.path.basename(text_decoded).replace('_', ' ')

def wiki_get_text_from_link(link):
    return get_wiki_page(link)

def wiki_handler(link, text):
    wiki_links = ()
    wiki_page = get_wiki_page(link)

    if wiki_page:
        page_wiki_link = '[{0} {1}]'.format(link, wiki_page)

        wiki_links = (
            {
                "title": link,
                "subtitle": "wiki page url",
                "arg": link
            },
            {
                "title": page_wiki_link,
                "subtitle": "wiki page wiki txt",
                "arg": page_wiki_link
            },
        )
    
    return wiki_links
