
import csv, datetime

with open('EURONEXT-INFY.csv', 'rb') as infy:
    infy2 = csv.DictReader(infy)
    for row in infy2:
        print datetime.datetime.strptime(row['Date'], '%Y-%m-%d').year,\
            row['Last']


# JSON - Module data read