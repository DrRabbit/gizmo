import csv
from datetime import datetime
from bisect import bisect_left


def find_closest_dt(dt, tempDt):
    searchDt = datetime.strptime(tempDt, '%d-%m-%Y').date()
    if searchDt < dt[0] or searchDt > dt[len(dt)-1]:
        return -1
    else:
        pos = bisect_left(dt, searchDt)
        if dt[pos] == searchDt:
            return pos
        else:
            return pos-1

path = 'C:\\Users\\Alex\\Desktop\\timeSeries.csv'
dt = []
px = []

f = open(path)
reader = csv.reader(f)

for row in reader:
    tempDt = datetime.strptime(row[0], '%d/%m/%Y').date()
    dt.append(tempDt)
    tempPx = float(row[1])
    px.append(tempPx)
f.close()

# don't use '23/01/2002' because even in the ' ' the backslash is a function
searchStrDt = '04-11-2015'
pos = find_closest_dt(dt, searchStrDt)

if pos != -1:
    print 'searchDt = ', searchStrDt, ', pos = ', pos, ' date = ', dt[pos]
else:
    print 'searchDt = ', searchStrDt, 'pos = ', pos, 'date = '
