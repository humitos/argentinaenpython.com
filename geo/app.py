import os
import sys

# HORRIBLE HACK
sys.path.append(os.path.join('..', 'web'))
import geocoder

import logging
from geolocation import (
    calc_my_position_address,
    save_json,
    setup_logging,
    logger,
    MY_POSITION_FILENAME
)
from flask import Flask, render_template, request


setup_logging(True)

# Test it from console:
#  curl http://127.0.0.1:5000/ajax/geolocation/ -X POST -F lat=-26.1852983 -F lon=-58.1744976

app = Flask(__name__)


@app.route("/ajax/", methods=['POST'])
def geolocation():
    lat = request.form['lat']
    lon = request.form['lon']

    logger.info('Lat: %s - Lon: %s', lat, lon)

    # get address from lat, lon
    response = geocoder.mapquest('{}, {}'.format(lat, lon))
    if response.status_code == 200:
        address = '{}, {}, {}'.format(
            response.city,
            response.province,
            response.country
        )
        response = calc_my_position_address(
            address,
            MY_POSITION_FILENAME,
            upload=False
        )
        output = os.path.join('assets', 'data', 'my-position.json')
        save_json(response.latlng, output)

    return 'OK'


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
