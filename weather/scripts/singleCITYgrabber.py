## Grabs data for a single WBAN from the raw data

import csv
import glob
import os
import sys


## First, create a dict with the WBAN as key and the city name as value

dict = {'99999': 'BATTERY','94728':'CENTRAL PARK','94706':'CENTRAL PARK B','14709':'BRONX COUNTY','14786':'QUEENS','94789':'JFK','14732':'LGA'}

## Now, using Python's glob module, run a cleaning operation on all files in the folder, resulting in a single file

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
				if row[0] in dict:
					row[0]=dict[row[0]]
					filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[24],row[40]))
                else:
                        header = next(filereader,None)
                        for row in filereader:
                        	row[4]=row[4][0:3]
				if row[0] in dict:
					row[0]=dict[row[0]]
					filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[24],row[40]))       
        file_counter += 1
