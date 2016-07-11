#!/usr/bin/python
# -*- coding: utf-8 -*-

"for monitor host's information"

import sys
import psutil
import json

def _cpu(args, args_num):
    result = []
    for i in range(args_num):
        try:
            getattr(psutil, args[i])
        except AttributeError as e:
            print e
            continue
        result.append(getattr(psutil, args[i])())
    return result

def json_data(sysinfo_list):
    return json.dumps(sysinfo_list)

if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len > 2:
        args_num = args_len - 2
        args = [sys.argv[x] for x in range(2, args_len)]
        result = _cpu(args, args_num)
        print result
        print type(json_data(result)),json_data(result)
    else:
        print "ERROR: too less arguments!"
