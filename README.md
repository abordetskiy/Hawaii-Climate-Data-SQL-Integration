# SQLAlchemy Challenge - Surfs Up! - Honolulu Vacation

# sqlalchemy-Challenge.ipynb:   An analysis of Hawaii Climate Temperature data. It reads an sqlite database using the SQLAlchemy module to query, inspect, and transform the data to provide insight into weather patterns.

    # The first graph shows the precipitation over the last 12 months prior to the last entry date. You can see that there are spikes in precipitation accross the board, but the longest dip seems to be just before November. The data for this graph was outputted as a CSV for reading by app.py

    # The Station Dataframe shows the Station names, IDs, and entry counts (how many pieces of data came from that station). Also provided is a show of temperature statistics fo the most active station. The data for this graph was outputted as a CSV for reading by app.py

    # The second graph uses the last 12 months of temperature data from only the most active station (Waihee). The most common temperature was ~75(F) and ranged from ~60(F)~85(F)

    # BONUS ANALYSES:

    # Temperature Analysis I pulls temperature data from all stations for June and December. It then runs these numbers through Welch's T-Test to get a pvalue=5.3283128862831936e-05. Based on our limited data points, it seems that differences between June and December temperatures in Hawaii are statistically significant

    # Temperature Analysis II pulls temperature data for dates one year prior to user inputted start and end dates. I plots these on a bar graph with a vertical error bar. Using a date range of 2016-10-25 - 2016-11-10 (a wonderful two week vacation) shows me an average temperature of around 64(F) with error bar showing between 57(F) and 70(F).


# app.py: A web app that provides access to the output from the analysis by querying sqlite database and reading CSV file output from .ipynb script. Please use %Y-%m-%d (YYYY-MM-DD) format when entering dates into searchbar.

