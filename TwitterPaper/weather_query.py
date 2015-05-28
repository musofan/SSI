import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

filewriter = csv.writer(open(output_file,'wb'))
file_counter = 0

for input_file in glob.glob(os.path.join(input_path,'*.txt')):
    with open(input_file,'rU') as txt_file:
        filereader = csv.reader(txt_file)
        if file_counter < 1:
            for row in filereader:
                filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[22],row[24],row[40]))
        else:
            header = next(filereader,None)
            for row in filereader:
                filewriter.writerow((row[0],row[1],row[2],row[4],row[10],row[22],row[24],row[40]))       
    file_counter += 1