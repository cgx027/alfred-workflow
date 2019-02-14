import os
import sys
from optparse import OptionParser

def get_single_user_input(query='', index=1):
    if not query and len(sys.argv) < 2:
        return None
    query_data = query or sys.argv[1]
    params = query_data.split()
    if len(params) >= index:
        return params[index - 1]
    else:
        return None

def get_user_link_txt(query=''):
    ''' return link text provided by user, the following user text will be returned
    command line:
        l link 'user link text with space in it'
    '''

    if not query and len(sys.argv) < 2:
        return None
    query_data = query or sys.argv[1]
    params = query_data.split()
    if len(params) >= 2:
        return ' '.join(params[1:])
    else:
        return None

def get_all_user_input(query=''):
    params = query or sys.argv[1]
    return params

def get_user_input_count(query=''):
    if not query and len(sys.argv) < 2:
        return 0
    query_data = query or sys.argv[1]
    params = query_data.split()
    return len(params)
