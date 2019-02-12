import re

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