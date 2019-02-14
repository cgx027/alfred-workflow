import os
import re
try:
    from urllib.parse import unquote
except:
    from urllib import unquote
from .strings import extractByRegex

# https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template
# https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study
CONF_HTTP_PREFIX = 'https://confluence.eng.vmware.com/'
PATTERN_DISPLAY = r'https://confluence.eng.vmware.com/display/(.*)/(.*)'
PATTERN_PAGES = r'https://confluence.eng.vmware.com/pages/viewpage.action\?spaceKey=(.*)&title=(.*)'
PATTERN_DISPLAY_SPACE = r'https://confluence.eng.vmware.com/display/(.*)'
PATTERN_PAGES_SPACE = r'https://confluence.eng.vmware.com/pages/viewpage.action\?spaceKey=(.*)'

def get_space_title(text):
    text_decoded = unquote(text)
    matched = False
    if 'http' in text_decoded and not text_decoded.startswith(CONF_HTTP_PREFIX):
        return None, None
    for pattern in [PATTERN_DISPLAY, PATTERN_PAGES]:
        conf_info = extractByRegex(pattern, text_decoded)
        if conf_info:
            space, title = conf_info
            matched = True
            return space, title.replace('+', ' ')
    for pattern in [PATTERN_DISPLAY_SPACE, PATTERN_PAGES_SPACE]:
        space = extractByRegex(pattern, text_decoded)
        if space:
            matched = True
            return space, None
    if not matched:
        return None, None


def conf_get_text_from_link(link):
    space, title = get_space_title(link)
    if title:
        return title.replace('+', ' ')
    if space:
        return space
    return 'confluence link'

def confluence_handler(link, text):
    confluence_links = ()
    space, title = get_space_title(link)
    # print(space, title)

    if space:
        space_link = os.path.join(CONF_HTTP_PREFIX, 'display', space)
        link_with_user_text = link + ' ' + text if text else link
        page_wiki_link = '[{0} {1}]'.format(link, text or title or space)

        confluence_links = (
            {
                "title": link_with_user_text,
                "subtitle": "confluence page url",
                "arg": link_with_user_text
            },
            {
                "title": page_wiki_link,
                "subtitle": "confluence page wiki txt",
                "arg": page_wiki_link
            },
            {
                "title": space_link,
                "subtitle": "confluence space url",
                "arg": space_link
            },
        )
    
    return confluence_links
