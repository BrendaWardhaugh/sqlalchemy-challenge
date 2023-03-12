import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

#import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Stations = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )
# Calculations

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create a session
    session = Session(engine)

    """Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using"""
    # Query the results from your precipitation analysis

    day_1year = dt.date(2017,8,23) - dt.timedelta(days = 365)
    prcp_scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >=day_1year).all()
    
    session.close()
    #Create a dictionary from the row data and append to a list of all results
    prcp_results = []
    for date, prcp in prcp_scores:
        results_dict ={}
        results_dict["date"] = date
        results_dict["prcp"] = prcp
        prcp_results.append(results_dict)
    return jsonify(prcp_results)
   
@app.route("/api/v1.0/stations")
def stations():
    #Create a session
    session = Session(engine)
    #Query all stations
    station = session.query(Stations.station).all()
    session.close()
    #convert list of tuples into normal list
    all_stations = list(np.ravel(station))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    #Create a session
    session = Session(engine)
    # Design a query to find the most active stations (i.e. what stations have the most rows?)
    # List the stations and the counts in descending order.
    active_stations = session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    temps = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.station ==active_stations[0][0]).all()[0]
    session.close()
    # Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
    
    temps_list = list(np.ravel(temps))
    return jsonify(temps_list)

@app.route("/api/v1.0/<start>")
    #Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
def startDateOnly(start=None):
    session = Session(engine)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    start_1 = dt.datetime.strptime(start, "%m-%d-%Y")
    results = session.query(*sel).filter(Measurement.date >= start_1).all()
    session.close()
    temps = list(np.ravel(results))
    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start=None,end=None):
    session = Session(engine)    
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    start_1 = dt.datetime.strptime(start, "%m-%d-%Y")
    results = session.query(*sel).filter(Measurement.date >= start_1).all()
    session.close()
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == '__main__':
    app.run()
   


    