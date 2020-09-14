# Import Dependencies
from flask import Flask, jsonify
import pandas as pd
import json
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# Included check_same_thread parameter to avoid errors when running multiple instances in same app
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread':False})
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables 
Base.prepare(engine,reflect=True)

# Save references to each table
Measurement_Table = Base.classes.measurement
Station_Table = Base.classes.station

# Create our session (link) from Python to the DB
mySession = Session(bind=engine)

# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    TempStats =  mySession.query(func.min(Measurement_Table.tobs), func.avg(Measurement_Table.tobs), func.max(Measurement_Table.tobs)).\
        filter(Measurement_Table.date >= start_date).filter(Measurement_Table.date <= end_date).all()
    # Output in a proper dictionary format for return statement
    TempsStatsOutput = {"TMIN": TempStats[0][0],"TAVG":TempStats[0][2],"TMAX":TempStats[0][2]}
    return TempsStatsOutput
    
# Set up last date in series to referfence on <start> page
maxDate = dt.datetime.strptime(mySession.query(func.max(Measurement_Table.date))[0][0],'%Y-%m-%d')

# Initialize Flask
app = Flask(__name__)
# Flask Routes

@app.route("/")
def home():
    print("Home Page Accessed")
    return r'''Welcome to the Climate Analysis app page!<br>
    Available Routes:<br>
    <br>
    /api/v1.0/precipitation<br>
    /api/v1.0/stations<br>
    /api/v1.0/tobs<br>
    /api/v1.0/START_DATE<br>
        Example: /api/v1.0/2015-01-01<br>
    /api/v1.0/START_DATE/END_DATE<br>
        Example: /api/v1.0/2015-01-01/2016-01-01<br>
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

@app.route("/api/v1.0/<string:start>")
def Start(start):
    # Establish variables pulled from app route input and maxDate from query
    startDate = start
    endDate = maxDate
    # Call calc_temps to calculate stats and return to webpage
    jsonStart = calc_temps(startDate, endDate)
    print("start Page Accessed")
    return jsonStart

@app.route("/api/v1.0/<string:start>/<string:end>")
def StartEnd(start,end):
    # Establish variables pulled from app route input
    startDate = start
    endDate = end
    # Call calc_temps to calculate stats and return to webpage
    jsonStartEnd = calc_temps(startDate, endDate)
    print("start/end Page Accessed")
    return jsonStartEnd

if __name__ == "__main__":
    app.run(debug=False)
