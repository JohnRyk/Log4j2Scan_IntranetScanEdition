#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, make_response

ip = '172.17.0.1'

app = Flask(__name__)
@app.route('/getdomain.php',methods = ['GET'])
def index():
    resp = make_response(ip + ':53')  # 响应体
    resp.status = str(200)
        
    return resp

@app.route('/getrecords.php',methods = ['GET'])
def index1():
    with open('log','r') as f:
        resp = make_response(f.read())
#        lines = f.readlines()
#        latest = lines[-1]
#        print(latest)
#        resp = make_response(latest)  # 响应体
    resp.status = str(200)
        
    return resp

if __name__ == "__main__":
    print('http://'+ip+':18888/getdomain.php')
    print('http://'+ip+':18888/getrecords.php')
    app.run(processes=True,host="0.0.0.0", port=18888)
