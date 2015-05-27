import csv
with open('/home/damoncrockett/Desktop/weather/processedData/1st_order_wbans.txt','rb') as source:
	rdr = csv.reader( source )
	with open('/home/damoncrockett/Desktop/weather/processedData/wban.csv','wb') as result:
		wtr = csv.writer( result )
		for r in rdr:
			wtr.writerow((r[0],r[1],r[4]))
