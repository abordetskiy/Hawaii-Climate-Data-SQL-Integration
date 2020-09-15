# SQLAlchemy Challenge - Surfs Up! - Honolulu Vacation

# sqlalchemy-Challenge.ipynb:   An analysis of Hawaii Climate Temperature data. It reads an sqlite database using the SQLAlchemy module to query, inspect, and transform the data to provide insight into weather patterns.

    # The first graph shows the precipitation over the last 12 months prior to the last entry date. You can see that there are spikes in precipitation accross the board, but the longest dip seems to be just before November. The data for this graph was outputted as a CSV for reading by app.py

    # The Station Dataframe shows the Station names, IDs, and entry counts (how many pieces of data came from that station). Also provided is a show of temperature statistics fo the most active station. The data for this graph was outputted as a CSV for reading by app.py

    # The second graph uses the last 12 months of temperature data from only the most active station (Waihee). The most common temperature was ~75(F) and ranged from ~60(F)~85(F)

# app.py: A web app that provides access to the output from the analysis by querying sqlite database and reading CSV file output from .ipynb script. Please use %Y-%m-%d (YYYY-MM-DD) format when entering dates into searchbar.