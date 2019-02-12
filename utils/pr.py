import re
from .strings import extractByRegex

RE_PR = r'(\d{7})'
RE_PR_COMMENT = r'(\d{7})\#c(\d+)'
PR_HTTP_PREFIX = 'https://bugzilla.eng.vmware.com/'

def get_pr_number(text):
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
    pr_num, comment_num = extractByRegex(RE_PR_COMMENT, link)
    pr_num = extractByRegex(RE_PR, link)
    # print(pr_num_with_comment, pr_num)

    pr_text = "PR {0}#c{1}".format(pr_num, comment_num) if comment_num else "PR {0}".format(pr_num) if pr_num else 'link'
    return pr_text
