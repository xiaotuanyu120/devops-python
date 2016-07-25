#!./env/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from rrdtool import create_rrd, update_rrd

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    data = _encode_it(request.get_json())
    if not data:
        print "Error: don't get any data"
        return "Null"
    req_host = request.host.split(':')[0]
    monitor_item = data.keys()[0]
    update_data = data[monitor_item]
    rrdb_name = 'rrdtool/%s-%s.rrd' % (req_host, monitor_item)
    try:
        update_rrd(rrdb_name, update_data['time'], update_data[monitor_item])
    except:
        create_rrd(req_host, monitor_item, step=5)
        update_rrd(rrdb_name, update_data['time'], update_data[monitor_item])
    print data, type(data)
    return str(data)


def _encode_it(data):
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, list):
        return [_encode_it(x) for x in data]
    elif isinstance(data, dict):
        return dict([(_encode_it(key), _encode_it(value))
                    for key, value in data.iteritems()])
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
