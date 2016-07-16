#!./env/bin/python
# -*- coding: utf-8 -*-

import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    data = request.get_json()
    if not data:
        return "Null"
    print _encode_it(data), type(_encode_it(data))
    return str(_encode_it(data))


def _encode_it(data):
    if isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, list):
        return [_encode_it(x) for x in data]
    elif isinstance(data, dict):
        return dict([(_encode_it(key), _encode_it(value)) for key, value in data.iteritems()])
    return data
# python3
# return {
#     _encode_it(key): _encode_it(value) for key, value in data.iteritems()
# }


if __name__ == '__main__':
    app.run(host='0.0.0.0')
