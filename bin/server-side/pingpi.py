#!/usr/bin/python3

'''This script is designed to be run every minute by a cron job. It sends a
accepts: url and port number as command line args
data packet to a particular IP and port, as specified by ENV VARs
'''
import datetime
import json
import sys
import requests

if __name__ == "__main__":

    # url = sys.argv[1]
    # port = sys.argv[2]
    url = 'http://larmalade.getmyip.com'
    port = '53154'
    url = url + ':' + port

    d = {}
    # print(json.dumps(d))
    d['date'] = datetime.datetime.now()

    def myconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    payload = json.dumps(d, default=myconverter)
    print(payload)

    r = requests.post(url, data=payload)
