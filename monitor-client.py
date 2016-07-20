#!./env/bin/python
# -*- coding: utf-8 -*-

"monitor client"

import sys
import json
import urllib2
import monitor_scripts


def json_post(url, data, header):
    'transfer data to json format and send it by using http to url'
    jdata = json.dumps(data, ensure_ascii=False)
    req = urllib2.Request(url, jdata, headers=header)
    response = urllib2.urlopen(req)
    return response.read()


def get_mon_data(data):
    mon_data = {}
    if isinstance(data, str):
        mon_data[data] = getattr(monitor_scripts, data)()
    elif isinstance(data, list):
        for item in data:
            try:
                item_d = getattr(monitor_scripts, item)()
            except:
                print sys.exe_info()[0]
                continue
            mon_data[item] = item_d
    return mon_data


def get_args(args):
    args_len = len(args)
    if args_len == 2:
        return args[1]
    elif args_len > 2:
        return [args[x] for x in range(1, args_len)]
    else:
        print "ERROR: too less arguments!"
        return


if __name__ == "__main__":
    mon_items = get_args(sys.argv)
    mon_data = get_mon_data(mon_items)
    header = {'Content-type': 'application/json'}
    url = "http://127.0.0.1:5000/"
    json_post(url, mon_data, header=header)
