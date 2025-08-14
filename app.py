from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
environment_data = {
    "temperature": 0,
    "humidity": 0,
    "water_level": 0,
    "soil_moisture": 0
}
settings = {
    "min_temperature": 0,
    "max_temperature": 0,
    "min_humidity": 0,
    "max_humidity": 0
}
@app.route("/api/data/environment", methods=["GET"])
def get_environment_data():
    return jsonify(environment_data), 200
@app.route("/api/data/settings", methods=["GET"])
def get_settings():
    return jsonify(settings), 200
@app.route("/api/data/environment", methods=["POST"])
def update_environment_data():
    global environment_data
    v = request.get_json(silent=True) or {}
    print("Received /environment POST:", v)
    t = v.get("temperature", environment_data["temperature"])
    h = v.get("humidity", environment_data["humidity"])
    l = v.get("water_level", environment_data["water_level"])
    s = v.get("soil_moisture", environment_data["soil_moisture"])

    new_data = {
        "temperature": t,
        "humidity": h,
        "water_level": l,
        "soil_moisture": s
    }
    environment_data.update(new_data)
    print("Updated environment data:", environment_data)
    return jsonify({"status": "ok", "received": new_data}), 201
@app.route("/api/data/settings", methods=["POST"])
def update_settings():
    global settings
    v = request.get_json(silent=True) or {}
    print("Received /settings POST:", v)
    tmin = v.get("min_temperature", settings["min_temperature"])
    tmax = v.get("max_temperature", settings["max_temperature"])
    hmin = v.get("min_humidity", settings["min_humidity"])
    hmax = v.get("max_humidity", settings["max_humidity"])

    new_settings = {
        "min_temperature": tmin,
        "max_temperature": tmax,
        "min_humidity": hmin,
        "max_humidity": hmax
    }
    settings.update(new_settings)
    print("Updated settings:", settings)
    return jsonify({"status": "ok", "received": new_settings}), 201
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
