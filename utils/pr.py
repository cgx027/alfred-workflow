import re
from .strings import extractByRegex

RE_PR = r'(\d{7})'
PR_HTTP_PREFIX = 'https://bugzilla.eng.vmware.com/show_bug.cgi?id='

def get_pr_number(text):
    return extractByRegex(RE_PR, text)

def get_url_from_number(num):
    return '{0}{1}'.format(PR_HTTP_PREFIX, num)
    