import re
import subprocess

def extractByRegex(expression, text):
    ''' Extract subtext from input text according to regex expression passed in

    Return:
        String: if only one hit is found
        List of Strings: if multiple hits are found
    '''
    # express has to contain a regex group
    reMatch = re.search(expression, text)
    if reMatch:
        if len(reMatch.groups()) > 1:
            # return a tuple for easy unpack if match group is larger than 1
            return reMatch.groups()
        # return a single string if only one group
        return reMatch.group(1)
    return None

def convert_to_html_anchor(link, text):
    '''convert a link to html anchor'''
    return '<a href=\"{0}\">{1}</a>'.format(link, text)

def transform_to_RTF(html):
    p = subprocess.Popen(['textutil','-format','html','-convert','rtf','-stdin','-stdout'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.write(html.encode('utf-8'))
    p.stdin.close()
    retcode = p.wait()
    data = p.stdout.read()
    return data

def set_clipboard_data(data):
    ''' copy data to clipboard '''
    p = subprocess.Popen(['pbcopy','Prefer','rtf'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()
