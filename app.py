from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
data = {
    "nhietdo": 0,
    "doam": 0,
    "luongnuoc": 0,
    "doamdat": 0
}
value = {
    "nhietdotoithieu": 0,
    "nhietdotoida": 0,
    "doamtoithieu": 0,
    "doamtoida": 0
}
@app.route("/api/data/moitruong", methods=["GET"])
def output_data1():
    return jsonify(data), 200
@app.route("/api/data/caidat", methods=["GET"])
def output_data2():
    return jsonify(value), 200
@app.route("/api/data/moitruong", methods=["POST"])
def input_data1():
    global data
    v = request.get_json(silent=True) or {}
    print("Received /moitruong POST:", v)
    t = v.get("nhietdo", data["nhietdo"])
    h = v.get("doam", data["doam"])
    l = v.get("luongnuoc", data["luongnuoc"])
    d = v.get("doamdat", data["doamdat"])
    new_data = {
        "nhietdo": t,
        "doam": h,
        "luongnuoc": l,
        "doamdat": d
    }
    data.update(new_data)
    print("Updated data:", data)
    return jsonify({"status": "ok", "received": new_data}), 201
@app.route("/api/data/caidat", methods=["POST"])
def input_data2():
    global value
    v = request.get_json(silent=True) or {}
    print("Received /caidat POST:", v)
    tmin = v.get("nhietdotoithieu", value["nhietdotoithieu"])
    tmax = v.get("nhietdotoida", value["nhietdotoida"])
    hmin = v.get("doamtoithieu", value["doamtoithieu"])
    hmax = v.get("doamtoida", value["doamtoida"])
    new_value = {
        "nhietdotoithieu": tmin,
        "nhietdotoida": tmax,
        "doamtoithieu": hmin,
        "doamtoida": hmax
    }
    value.update(new_value)
    print("Updated value:", value)
    return jsonify({"status": "ok", "received": new_value}), 201
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
