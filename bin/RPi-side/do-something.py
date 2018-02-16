#!/usr/bin/python3

'''This file contains things-to-do, aka functions that can be triggered by
an http request hitting the get-server program'''

include datetime

file_path = "time_stamps.tx"

def append_timestamp(fname):
	'''append timestamp to a file full of timestamps!
	'''
	json_time = datetime.datetime.now()
	with open(file_path, mode='a', encoding='utf-8') as f:
		f.write(
