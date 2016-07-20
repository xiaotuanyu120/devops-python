#!./env/bin/python
# -*- coding: utf-8 -*-

import psutil
import sys
import time


def cpu_info(args, args_num):
    result = {}
    result['item'] = 'cpu'
    result['time'] = time.time()
    for i in range(args_num):
        try:
            getattr(psutil, args[i])
        except AttributeError as e:
            print e
            continue
        result[args[i]] = getattr(psutil, args[i])()
    return result


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len > 2:
        args_num = args_len - 2
        args = [sys.argv[x] for x in range(2, args_len)]
        print cpu_info(args, args_num)
    else:
        print "ERROR: too less arguments!"
