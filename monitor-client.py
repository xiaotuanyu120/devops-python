#!./env/bin/python
# -*- coding: utf-8 -*-

"for monitor host's information"

import sys
import psutil
import json
import urllib2
import socket

import cpu_m


def get_ip():
    'get ip address of the client'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        e = sys.exc_info()[0]
        return
    finally:
        s.close()
    return ip


def json_post(url, data, header):
    'transfer data to json format and send it by using http to url'
    jdata = json.dumps(data, ensure_ascii=False)
    req = urllib2.Request(url, jdata, headers=header)
    response = urllib2.urlopen(req)
    return response.read()


if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len > 2:
        args_num = args_len - 2
        args = [sys.argv[x] for x in range(2, args_len)]
        cpu_result = cpu_m.cpu(args, args_num)
        result = {}
        result[get_ip()] = cpu_result
        headers = {'Content-type':'application/json',}
        url = "http://127.0.0.1:5000/"
        json_post(url, result, header=headers)
    else:
        print "ERROR: too less arguments!"
