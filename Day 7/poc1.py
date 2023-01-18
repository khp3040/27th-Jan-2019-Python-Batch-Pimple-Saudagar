infy = open('EURONEXT-INFY.csv', 'r')

year_last = dict()
for row in infy:
    row = row.strip()
    if row.startswith('Date'):
        continue
    columns = row.split(',')
    year = columns[0].split('-')[0]
    if year in year_last:
        year_last[year].append(float(columns[3]))
    else:
        year_last[year] = list()
        year_last[year].append(float(columns[3]))

for year, last in sorted(year_last.items(), key=lambda x:x[0]):
    print year, sum(last)/len(last)

