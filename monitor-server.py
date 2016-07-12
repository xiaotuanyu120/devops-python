#!/root/env26/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_data():
    data = request.data
    #if not data:
    #    data = request.form.keys()[0] 
    #    print 'key' + data
    #    return data
    print data
    return data


if __name__ == '__main__':
    app.run()
