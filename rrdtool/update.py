#!/usr/env27/bin/python
# -*- coding: utf-8 -*-

import rrdtool
import time
import psutil

total_input_traffic = psutil.net_io_counters()[1]
total_output_traffic = psutil.net_io_counters()[0]
starttime = int(time.time())
update = rrdtool.updatev(
    '/root/rrdtool/Flow.rrd',
    '%s:%s:%s' % (
        str(starttime),
        str(total_input_traffic),
        str(total_output_traffic)
    ),
)

if __name__ == "__main__":
    print starttime
    print total_input_traffic
    print total_output_traffic
