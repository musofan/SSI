## Cleaner script for hourly weather data files from NCDC's QCLCD database: http://cdo.ncdc.noaa.gov/qclcd
## Also uses a table from http://www.weather2000.com that links first-order WBAN station numbers with city names

import csv
import glob
import os
import sys


## First, create a dict from the WBAN table:

with open('wban.csv','rw') as infile:
	reader = csv.reader(infile)
	wban_dict = {rows[2]:rows[1] for rows in reader}
infile.close()

## Now, using Python's glob module, run a cleaning operation on all files in the folder:
## Results in a single file, weather2013.csv.

input_path = sys.argv[1]
output_file = sys.argv[2]

filewriter = csv.writer(open(output_file,'wb'))
file_counter = 0
for input_file in glob.glob(os.path.join(input_path,'*.txt')):
        with open(input_file,'rU') as txt_file:
                filereader = csv.reader(txt_file)
                if file_counter < 1:
                        for row in filereader:
				row[4]=row[4][0:3]
				if row[0] in wban_dict:
					row[0]=wban_dict[row[0]]
					filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[24],row[40]))
                else:
                        header = next(filereader,None)
                        for row in filereader:
                        	row[4]=row[4][0:3]
				if row[0] in wban_dict:
					row[0]=wban_dict[row[0]]
					filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[24],row[40]))       
        file_counter += 1
