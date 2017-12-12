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


idsList = []
for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/accounts'):
    with open('C:/Users/jyifa/Desktop/Si608/project/accounts/' +file) as ids:
        idsList.append(json.load(ids))
idsList = list(chain.from_iterable(idsList))

create_time = pd.DataFrame(idsList)['created_at']
url_list = pd.DataFrame(idsList)['url']

# print(len(create_time))
# print(len(url_list))

local_user_create_time = []
for index, url in enumerate(url_list):
    try:
        words = url.split("/")
        instance = words[2]
        if instance == "mastodon.social":
            local_user_create_time.append(create_time[index])
    except:
        continue

# print(local_user_create_time)
format = "%Y-%m-%d"
covert_user_create_time = []
for time in local_user_create_time:
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
plt.ylabel('# of local users created')
locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
plt.show()