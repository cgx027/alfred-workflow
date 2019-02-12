import os
import sys
from optparse import OptionParser

def get_single_user_input():
    if len(sys.argv) >= 2:
        return sys.argv[1]