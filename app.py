# Import Dependencies
from flask import Flask, jsonify
import pandas as pd
import csv
import os
# Initialize Flask
app = Flask(__name__)
# Flask Routes

@app.route("/")
def home():
    print("Home Page Accessed")
    return '''Welcome to the Climate Analysis app page!<br>
    Available Routes:<br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/<start><br>
    /api/v1.0/<start>/<end><br>
    
    Please enter all dates in a %Y-%m-%d (YYYY-MM-DD) format
    '''

@app.route("/api/v1.0/precipitation")
def Precipitation():
    #csvpath = os.path.join("Resources","Last12moPrcp.csv")
    Last12moPrcp = pd.read_csv("Last12moPrcp.csv")
    jsonPrecipitation = jsonify(Last12moPrcp)
    print("precipitation Page Accessed")
    return jsonPrecipitation

@app.route("/api/v1.0/stations")
def Stations():
    #jsonStations = jsonify(PLACEHOLDER)
    jsonStations = "#"
    print("stations Page Accessed")
    return jsonStations

@app.route("/api/v1.0/tobs")
def Tobs():
    #jsonTemps = jsonify(PLACEHOLDER)
    jsonTemps = "#"
    print("tobs Page Accessed")
    return jsonTemps

@app.route("/api/v1.0/<start>")
def Start():
    #jsonStart = jsonify(PLACEHOLDER)
    jsonStart = "#"
    print("start Page Accessed")
    return jsonStart

@app.route("/api/v1.0/<start>/<end>")
def StartEnd():
    #jsonStartEnd = jsonify(PLACEHOLDER)
    jsonStartEnd = "#"
    print("start/end Page Accessed")
    return jsonStartEnd

if __name__ == "__main__":
    app.run(debug=False)
