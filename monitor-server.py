#!./env/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from rrdtool import update

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    data = _encode_it(request.get_json())
    if not data:
        print "Error: don't get any data"
        return "Null"
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
