#!/usr/env27/bin/python

import rrdtool
import time
import psutil


def update_rrd(rrd_name, time, data1):
    update = rrdtool.updatev(
        rrd_name,
        '%s:%s' % (str(starttime), str(data1))
    )
