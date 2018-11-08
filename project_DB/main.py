from flask import (Flask, render_template, request, jsonify)
from models.device import Device, DeviceLocation
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    return "List of products"


@app.route('/devices/location/ping',  methods=['POST'])
def record_location():
    ping_data = dict(request.form.items())
    DeviceLocation.create(
        lat=ping_data.get('lat'),
        long=ping_data.get('long'),
        alt=ping_data.get('alt'),
        dev_id=ping_data.get('dev_id'),
    )
    result = {'status': 'success'}
    return jsonify(result)


@app.route('/devices/location/<dev_id>',  methods=['GET'])
def last_known_location(dev_id='1'):
    device_loc = (DeviceLocation
                  .select()
                  .where(DeviceLocation.dev_id == dev_id)
                  .order_by(DeviceLocation.time_ping.desc())
                  .get()
                  )
    results = {
        'dev_id': dev_id,
        'lat': device_loc.dev_id,
        'long': device_loc.long,
        'alt': device_loc.alt,
        'timestamp': device_loc.time_ping
        }
    return jsonify(results)

@app.route('/test', methods=['POST', 'GET'])
def test_arduino():
  return "success"


if __name__ == '__main__':
    app.run(**app_start_config)