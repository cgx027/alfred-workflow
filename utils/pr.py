import re
from .strings import extractByRegex

RE_PR = r'(\d{7})'
RE_PR_COMMENT = r'(\d{7})\#c(\d+)'
PR_HTTP_PREFIX = 'https://bugzilla.eng.vmware.com/'

def get_pr_number(text):
    if 'http' in text and not text.startswith(PR_HTTP_PREFIX):
        return None, None

    pr_info = extractByRegex(RE_PR_COMMENT, text)
    if pr_info:
        return pr_info

    pr_num = extractByRegex(RE_PR, text)
    if pr_num:
        return pr_num, None
    return None, None

def get_url_from_number(pr_num, comment_num):
    if comment_num:
        return '{0}show_bug.cgi?id={1}#c{2}'.format(PR_HTTP_PREFIX, pr_num, comment_num)
    return '{0}show_bug.cgi?id={1}'.format(PR_HTTP_PREFIX, pr_num)

def pr_get_text_from_link(link):
    pr_info = extractByRegex(RE_PR_COMMENT, link)
    if pr_info:
        pr_num, comment_num = extractByRegex(RE_PR_COMMENT, link)
    else:
        pr_num = extractByRegex(RE_PR, link)
        comment_num = None
    # print(pr_num_with_comment, pr_num)

    pr_text = "PR {0}#c{1}".format(pr_num, comment_num) if comment_num else "PR {0}".format(pr_num) if pr_num else 'link'
    return pr_text

def pr_handler(link, text):
    pr_links = ()

    pr_num, comment_num = get_pr_number(link)
    if pr_num:
        pr_url = get_url_from_number(pr_num, comment_num)
        pr_url_with_user_input = pr_url + ' ' + text if text else pr_url
        if comment_num:
            wiki_text = text or "{0}#{1}".format(pr_num, comment_num)
            wiki_link = '[{0} PR {1}]'.format(pr_url, wiki_text)
            short_desc = 'PR {0}#c{1}'.format(pr_num, comment_num)
        else:
            wiki_text = text or "{0}".format(pr_num)
            wiki_link = '[{0} PR {1}]'.format(pr_url, wiki_text)
            short_desc = 'PR {0}'.format(pr_num)
        pr_links = (
            {
                "title": pr_url_with_user_input,
                "subtitle": "full PR url",
                "arg": pr_url_with_user_input
            },
            {
                "title": wiki_link,
                "subtitle": "PR wiki link",
                "arg": wiki_link
            },
            {
                "title": short_desc,
                "subtitle": "PR short description",
                "arg": short_desc
            }
    )

    return pr_links
