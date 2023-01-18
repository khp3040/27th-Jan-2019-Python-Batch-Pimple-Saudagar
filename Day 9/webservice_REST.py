import requests, sys, json
from datetime import datetime
import logging

FORMAT = '%(levelname)s: %(message)s'

url = 'https://www.quandl.com/api/v3/datasets/EURONEXT/ADYEN.json?api_key=fKXsYh9Qi9ySbS8X6pNh'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filemode='w',
                    filename='myLog.log')

logging.debug('Hiting url {}'.format(url))
response = requests.get(url)

if response.status_code != 200: # Webservice didnt hit sucessfully
    logging.critical('Error: {}'.format(response.status_code))
    sys.exit(1)

content = response.content
dataset = json.loads(content) # as content is string thus used "loads"

logging.debug(content)

year_last = dict()
for row in dataset['dataset']['data']:
    year = datetime.strptime(row[0], '%Y-%m-%d').year
    last = float(row[4])
    if year in year_last:
        year_last[year].append(last)
    else:
        year_last[year] = list()
        year_last[year].append(last)

logging.info(str(year_last))
for year, last in year_last.items():
    print year, sum(last)/len(last)