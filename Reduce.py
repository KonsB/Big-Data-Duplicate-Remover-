#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
flag = False  # flag variable that works as a lock
              # False: haven't found a key with a different value
              # True: found a key with a different value FOR THE FIRST TIME
current_value = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py into two values key and value
    key, value = line.split()

    if flag is False and current_key == key and current_value != value:
        # the first time we find the same key with a different value change the flag to True
        # so that we print one time the line (key,value) with the same key as we want the key value pair
        # that appears at list two times with different value
        flag = True
        print('%s' % key)
    elif current_key != key:
        # else if the key is different from the previous one then and only then restart the value of the flag
        flag = False

    # store the current values
    current_key = key
    current_value = value







