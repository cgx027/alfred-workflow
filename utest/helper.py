''' Helper functions for unit test '''

import os
import json


def write_json(json_file, content, indent=4):
    ''' write object to json file '''
    with open(json_file, 'w+') as fout:
        json.dump(content, fout, indent=indent)


def read_json(json_file, dump=False):
    ''' Read json file and return object

        Print it to using 'print' if dump is set to true
    '''
    with open(json_file, 'r') as fin:
        content = json.load(fin)

    if dump:
        print(json.dumps(content, indent=4))

    return content


def dump_json(json_obj):
    ''' Dump json object to screen using print '''
    print(json.dumps(json_obj, indent=4))


def read_file(file_name):
    ''' Read json file and return object '''
    with open(file_name, 'r') as fin:
        content = fin.read()
    return content


def remove_file(file_name):
    try:
        os.remove(file_name)
    except:
        # ignore errors
        pass

def has_same_keys_in_object_list(result, expected_results, key):
    ''' check if two list of objects have the same keys '''
    try:
        keys = [item[key] for item in result]
        keys_expected = [item[key] for item in expected_results]
        keys.sort()
        keys_expected.sort()
    except:
        return False

    return keys == keys_expected