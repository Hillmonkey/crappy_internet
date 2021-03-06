#!/usr/bin/python3

'''This file contains things-to-do, aka functions that can be triggered by
an http request hitting the get-server program'''

import datetime

file_path = "time_stamps.txt"

def append_timestamp(fname):
    '''append timestamp to a file full of timestamps!
    '''
    json_time = datetime.datetime.now()
    with open(fname, mode='a', encoding='utf-8') as f:
        f.write(str(json_time) + '\n')
