#!/bin/env python

import psutil
import time


def cpu_percent():
    result = {}
    result['cpu_percent'] = psutil.cpu_percent(interval=0.5)
    result['time'] = time.time()
    return result
