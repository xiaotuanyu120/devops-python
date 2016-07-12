#!/root/env26/bin/python
# -*- coding: utf-8 -*-

"for monitor host's information"

import sys
import psutil
import json
import urllib2


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


# def json_data(sysinfo_list):
#     return json.dumps(sysinfo_list)


def json_post(url, sysinfo_list, headers):
    jdata = json.dumps(sysinfo_list)
    req = urllib2.Request(url, jdata, headers = headers)
    response = urllib2.urlopen(req)
    return response.read()


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len > 2:
        args_num = args_len - 2
        args = [sys.argv[x] for x in range(2, args_len)]
        result = _cpu(args, args_num)
#         print type(json_data(result)), json_data(result)
        headers = {
    'Content-type': 'binary/octet-stream',
#     'Content-length': len(postBody),
    'Content-transfer-encoding': 'binary',
}
        url = "http://127.0.0.1:5000/"
        json_post(url, result, headers)
    else:
        print "ERROR: too less arguments!"
