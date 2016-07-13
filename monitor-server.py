#!/root/env26/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_data():
    data = request.get_json()
    if not data:
        return "Null"
    return data


if __name__ == '__main__':
    app.run()
