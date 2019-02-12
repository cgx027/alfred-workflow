from utils.strings import *
from utils.input_output import *
from utils.pr import *

WIKI_PREFIX = "https://bugzilla.eng.vmware.com/"

def get_text_from_link(link):
    if link.startswith(WIKI_PREFIX):
        return pr_get_text_from_link(link)
    else:
        return 'link'

link = get_single_user_input()
if link.startswith('http'):
    link_text = get_text_from_link(link)
    link_html = convert_to_html_anchor(link, link_text)
    link_rtf = transform_to_RTF(link_html)
    set_clipboard_data(link_rtf)
else:
    set_clipboard_data(link)
# print(link, link_html, link_rtf)
# print(link_rtf)
