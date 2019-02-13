from utils.strings import *
from utils.input_output import *
from utils.pr import *
from utils.nfs import *
from utils.confluence import *
from utils.wiki import *
from link.default import *

PR_PREFIX = "https://bugzilla.eng.vmware.com/"
NFS_HTTP_PREFIX = 'http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/'
CONF_HTTP_PREFIX = 'https://confluence.eng.vmware.com/'
WIKI_HTTP_PREFIX = 'https://wiki.eng.vmware.com/'

def get_text_from_link(link):
    if link.startswith(PR_PREFIX):
        return pr_get_text_from_link(link)
    if link.startswith(NFS_HTTP_PREFIX):
        return nfs_get_text_from_link(link)
    if link.startswith(CONF_HTTP_PREFIX):
        return conf_get_text_from_link(link)
    if link.startswith(WIKI_HTTP_PREFIX):
        return wiki_get_text_from_link(link)
    else:
        return None
    if get_user_input_count():
        # use user input as text if a second param is used
        return get_text_from_user_input()
    else:
        return 'link'

def run(query=''):
    link = get_single_user_input(query)
    all_input = get_all_user_input(query)

    # less than 2 input and it's not a hyperlink
    is_less_than_2_and_not_hyper = get_user_input_count(query) < 2 and not link.startswith('http')
    # a plain text with no dot in link
    is_plain_text = get_user_input_count(query) > 2 and '.' not in link
    # a wiki text
    is_wiki_text = link.startswith('[')

    if is_less_than_2_and_not_hyper or is_plain_text or is_wiki_text:
        set_clipboard_data(all_input.encode('utf-8'))
        return 'text', all_input, None
    else:
        link_text = get_text_from_link(link)
        if not link_text:
            link_text = get_text_from_user_input(query)
        if not link_text:
            # use default
            link_text = 'link'
        link_html = convert_to_html_anchor(link, link_text)
        link_rtf = transform_to_RTF(link_html)
        set_clipboard_data(link_rtf)
        return 'hyperlink', link, link_text

if __name__ == '__main__':
    run()
