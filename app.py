# Import Dependencies
from flask import Flask, jsonify
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# establish engine to sqlite file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables 
Base.prepare(engine,reflect=True)
# Save references to each table
Measurement_Table = Base.classes.measurement
Station_Table = Base.classes.station
# Create our session (link) from Python to the DB
mySession = Session(bind=engine)

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
    # Calculate the date 1 year ago from the last data point in the database
    # since session.query returns a tuple, we use [0][0] to get the value at the first entry
    # and datetime.strptime to convert it to a datetime object 
    # and subtract a year from it with dt.timedelta
    DatePrior12Mo = dt.datetime.strptime(mySession.query(func.max(Measurement_Table.date))[0][0],'%Y-%m-%d') - dt.timedelta(days=365)
    # Perform a query to retrieve the data and precipitation scores
    Last12moPrcp = mySession.query(Measurement_Table.prcp, Measurement_Table.date)
    # Save the query results as a Pandas DataFrame
    Last12moPrcp_df = pd.DataFrame(Last12moPrcp)
    # Rename columns to capitalize axis labels
    Last12moPrcp_df = Last12moPrcp_df.rename(columns = {"date":"Date","prcp":"Precipitation"})
    # Sort the dataframe by date
    Last12moPrcp_df = Last12moPrcp_df.sort_values(by="Date")
    # Set the index to the date column
    Last12moPrcp_df = Last12moPrcp_df.set_index("Date")
    # Turn dataframe into json
    jsonPrecipitation = jsonify(Last12moPrcp_df)
    #jsonPrecipitation = "#"
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
