#!./env/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    data = request.get_json()
    print data, jsonify(data), type(jsonify(data))
    if not data:
        return "Null"
    return jsonify(data)


if __name__ == '__main__':
    app.run()
