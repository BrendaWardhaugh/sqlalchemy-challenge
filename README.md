# sqlalchemy-challenge
Module 10 SQL

Please see the attached documents which include jupyter notebook script, app.py, and the rescourses.

This challenge was to imagine you've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area.Therefore, you use the csv data from local weather stations and sqlalchemy to search through the data to analysis the weather before selecting when you want to travel based on the conditions. Specifically examining the temperature and the precipitation.

Then, through the use of Flask, a website was created to view the precipitation over the last year, see which stations data was collected from, examine the lowest, highest, and average temperature from the most active station,and view the minimum temperature, the average temperature, and the maximum temperature for a specified date or date range.


## Exploratory Precipitation Analysis
Design a query to retrieve the last 12 months of precipitation data and plot the results using Pandas Plotting with Matplotlib.

![Prcp graph](https://user-images.githubusercontent.com/120147552/224552739-15c3448b-eda5-4f11-9182-0a6383047266.png)

## Exploratory Station Analysis
Using the most active station, query the last 12 months of temperature observation data for this station and plot the results as a histogram.

![hist temp](https://user-images.githubusercontent.com/120147552/224552805-31496bd9-963c-4bee-a49e-8d93b88f546e.png)

## Use of Flask to Create a Webpage
Webpage home page:

![webpage homepage](https://user-images.githubusercontent.com/120147552/224552963-6cee372b-e9d3-4b18-8b94-3e77693bd961.png)

Query the results from the precipitation analysis to create a dictionary of all results for the last year.

![webpage prcp](https://user-images.githubusercontent.com/120147552/224553050-7d6dc362-79f7-46c8-b9f8-17948e03827e.png)

List of all the stations used in the data set

![webpage stations](https://user-images.githubusercontent.com/120147552/224553093-188c40b5-cb52-48ac-bc29-fef1e5e31989.png)

The lowest, highest, and average temperature from the most active station.

![webpage tobs](https://user-images.githubusercontent.com/120147552/224553226-6737e61c-1111-46a1-a260-f0d4b8397863.png)

The minimum temperature, the average temperature, and the maximum temperature for October 23, 2016.

![Untitledebpage minimum temperature, the average temperature, and the maximum temperature for10-23-2016](https://user-images.githubusercontent.com/120147552/224553301-252f9b6e-d1c9-403b-8c34-f04b9d13e98e.png)

The minimum temperature, the average temperature, and the maximum temperature for June, 2017.

![webpage temps for june 2017](https://user-images.githubusercontent.com/120147552/224553359-6bfb1a4c-4586-4a76-b90c-501028079190.png)

