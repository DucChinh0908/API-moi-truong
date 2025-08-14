from flask import Flask, request, jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)
data = {
        "nhietdo" : 0,
        "doam" : 0,
        "luongnuoc" : 0,
        "doamdat" : 0
    }
value = {
        "nhietdotoithieu" : 0,
        "nhietdotoida" : 0,
        "doamtoithieu" : 0,
        "doamtoida" : 0
    }
@app.route("/api/data/moitruong",methods=["GET"])
def output_data1():
    return jsonify(data),201
@app.route("/api/data/caidat",methods=["GET"])
def output_data2():
    return jsonify(value),201
@app.route("/api/data/moitruong",methods=["POST"])
def input_data1():
    global data
    v = request.json
    t = v.get("nhietdo")
    h = v.get("doam")
    l = v.get("luongnuoc")
    d = v.get("doamat")
    new_data = {
        "nhietdo" : t,
        "doam" : h,
        "luongnuoc" : l,
        "doamdat" : d
    }
    data = new_data
    return jsonify({"type": "accept"}),201
@app.route("/api/data/caidat",methods=["POST"])
def input_data2():
    global value
    v = request.json
    tmin = v.get("nhietdotoithieu")
    tmax = v.get("nhietdotoida")
    hmin = v.get("doamtoithieu")
    hmax = v.get("doamtoida")
    new_value = {
        "nhietdotoithieu" : tmin,
        "nhietdotoida" :tmax,
        "doamtoithieu" : hmin,
        "doamtoida" : hmax
    }
    value = new_value
    return jsonify({"type": "accept"}),201
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)