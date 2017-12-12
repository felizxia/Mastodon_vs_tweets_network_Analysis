import time
import json
import datetime
import fnmatch
import os
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
from scipy.stats import norm


createTimeList = []
for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/AllData'):
    try:
        with open('C:/Users/jyifa/Desktop/Si608/project/AllData/' +file+'/accounts/accounts.json') as ids:
            id = json.load(ids)
            create_time = pd.DataFrame(id)['created_at']
            createTimeList.append(create_time[0])
    except:
        continue

# print(createTimeList)
# print(len(createTimeList))

format = "%Y-%m-%d"
covert_user_create_time = []
for time in createTimeList:
    date = time.split()[0]
    datetime_obj = datetime.strptime(date, format)
    covert_user_create_time.append(datetime_obj)
print(covert_user_create_time)
mpl_data = mdates.date2num(covert_user_create_time)

# plot it
fig, ax = plt.subplots(1,1)
ax.hist(mpl_data, bins=30, color='lightblue')
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))
plt.xlabel('Time')
plt.ylabel('# instance created')
locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
plt.show()