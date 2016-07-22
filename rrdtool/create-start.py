#!/bin/env python

from create_rrd import create_rrd


if __name__ == "__main__":
    #host = '10.10.180.23'.encode('ascii')
    host = '10.10.180.23'
    #ds_name = 'cpu_percent'.encode('ascii')
    ds_name = 'cpu_percent'
    step = '5'
    create_rrd(host, ds_name, step=step)
