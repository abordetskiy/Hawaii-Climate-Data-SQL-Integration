# Import Dependencies
from flask import Flask, jsonify
import pandas as pd
import json
# Initialize Flask
app = Flask(__name__)
# Flask Routes

@app.route("/")
def home():
    print("Home Page Accessed")
    return '''Welcome to the Climate Analysis app page!<br>
    Available Routes:<br>
    <br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/<start><br>
    /api/v1.0/<start>/<end><br>
    <br>
    NOTE: Please enter all dates in a %Y-%m-%d (YYYY-MM-DD) format
    '''

@app.route("/api/v1.0/precipitation")
def Precipitation():
    # Read output csv from .ipynb script
    jsonPrecipitation_df = pd.read_csv("Resources/Last12moPrcp.csv")
    # Convert dataframe to json format
    jsonPrecipitation_json = jsonPrecipitation_df.to_json(orient="index")
    # Creates json object capable of being parsed for pretty print
    jsonPrecipitation = json.loads(jsonPrecipitation_json)
    print("precipitation Page Accessed")
    return jsonPrecipitation

@app.route("/api/v1.0/stations")
def Stations():
    # Read output csv from .ipynb script
    jsonStations_df = pd.read_csv("Resources/StationCounts.csv")
    # Convert dataframe to json format
    jsonStations_json = jsonStations_df.to_json(orient="index")
    # Creates json object capable of being parsed for pretty print
    jsonStations = json.loads(jsonStations_json)
    print("stations Page Accessed")
    return jsonStations

@app.route("/api/v1.0/tobs")
def Tobs():
  # Read output csv from .ipynb script
    jsonTemps_df = pd.read_csv("Resources/MostActiveStationTemps.csv")
    # Convert dataframe to json format
    jsonTemps_json = jsonTemps_df.to_json(orient="index")
    # Creates json object capable of being parsed for pretty print
    jsonTemps = json.loads(jsonTemps_json)
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
