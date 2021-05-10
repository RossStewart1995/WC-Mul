from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import json

import mul

app = Flask(__name__)
@app.route('/')

def mul_func():

    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)

    if not x or not y:
        error_data = {
        "error":True,
        "string":"You must provide valid input for x/y"
        }
        error_reply = json.dumps(error_data, sort_keys=False)
        rx = Response(response=error_reply, status=400, mimetype="application/json")
        rx.headers["Access-Control-Allow-Origin"]="*"
        return rx

    mult = mul.multiply(x,y)

    data = {
        "error":False,
        "string":f"{x}*{y}={mult}",
        "author": "Ross Stewart",
        "answer":mult
    }

    reply = json.dumps(data, sort_keys=False)

    r = Response(response=reply, status=200, mimetype="application/json")
    r.headers["Access-Control-Allow-Origin"]="*"
    return r

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)