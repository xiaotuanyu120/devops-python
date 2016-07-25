#!/root/env27/bin/python

import rrdtool
import time


def create_rrd(host, ds_name, step=300):
    cur_time = str(int(time.time()))
    rrd_name = '%s-%s.rrd' % (host, ds_name)
    ds_str = 'DS:' + ds_name + ':COUNTER:10:0:U'

    rrd = rrdtool.create(
        rrd_name,
        '--step',
        step,
        '--start',
        cur_time,
        ds_str,
        'RRA:AVERAGE:0.5:1:600',
        'RRA:AVERAGE:0.5:6:700',
        'RRA:AVERAGE:0.5:24:775',
        'RRA:AVERAGE:0.5:288:797',
        'RRA:MAX:0.5:1:600',
        'RRA:MAX:0.5:6:700',
        'RRA:MAX:0.5:24:775',
        'RRA:MAX:0.5:444:797',
        'RRA:MIN:0.5:1:600',
        'RRA:MIN:0.5:6:700',
        'RRA:MIN:0.5:24:775',
        'RRA:MIN:0.5:444:797',
    )

    if rrd:
        print rrdtool.error()
    return
