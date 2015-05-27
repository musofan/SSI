Weather data from http://cdo.ncdc.noaa.gov/qclcd/
Data prepared by Damon Crockett, damoncrockett@gmail.com


The National Climatic Data Center (NCDC) collects readings from weather stations throughout the country. Stations are identified by a Weather Bureau Army Navy (WBAN) number. We obtained weather data from the above url for all of 2013 at a temporal resolution of ~15 minutes (it varies by station and month).

/rawData
	/2013xxhourly.txt
		There are 12 raw .txt files, downloaded directly from the above url. This is 'Quality-Controlled Local Climatological Data' (QCLCD). 

	/1st_order_wbans.txt	
		Downloaded from <http://www.weather2000.com/1st_order_wbans.txt>, gives city names for the major (i.e., 'first-order') weather stations. 			The resulting list of cities is essentially a list of (about 250) 'major' US cities.

	/qclcddocumentation.pdf
		PDF documentation for the QCLCD dataset, downloaded from <http://cdo.ncdc.noaa.gov/qclcd/qclcddocumentation.pdf>

/processedData
	/wban.csv
		This is a cleaned up version of 1st_order_wbans.txt, cleaned both by hand in a text editor, and by wbanCleaner.py. Some cities removed and added by hand.
	
	/weather2013.csv
		This is the final result of applying weatherCleaner.py to the 12 raw .txt files in /rawData (files of the form '2013xxhourly.txt').
		Its columns are city, date, time, sky cover, Fahrenheit temp, wind speed, and hourly precipitation. It drastically reduces the size of 			the data, because it eliminates from the raw qclcd any non-'major' weather stations. This file is ~2.5 million rows.


/scripts
	/wbanCleaner.py
		This script eliminates some columns of 1st_order_wbans.txt
	/weatherCleaner.py
		This script uses the python glob module to apply a cleaning operation to 12 raw QCLCD files (they are monthly). It eliminates many 			columns, any rows for non-major weather stations, and it truncates the 'sky cover' values. The result is a single file, weather2013.csv.
