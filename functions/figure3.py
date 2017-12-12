from mastodon import Mastodon
import time
import json
import datetime
import fnmatch
import os
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



idsList = []
for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/mastodon_blue'):
    with open('C:/Users/jyifa/Desktop/Si608/project/mastodon_blue/' +file) as ids:
        idsList.append(json.load(ids))
idsList = list(chain.from_iterable(idsList))

following = pd.DataFrame(idsList)['following_count']
statuses = pd.DataFrame(idsList)[['following_count','statuses_count']]

unique = {}
for i in following:
    if i not in unique:
        unique[i] = 1
    else:
        unique[i] += 1
print(unique)

following_statuses_mean = statuses.groupby(statuses['following_count'],as_index=False).mean()
following_statuses_median = statuses.groupby(statuses['following_count'],as_index=False).median()

x_median = []
y_median = []
for value in following_statuses_median.values:
    x_median.append(value[0])
    y_median.append(value[1])

x_mean = []
y_mean = []
for value in following_statuses_mean.values:
    x_mean.append(value[0])
    y_mean.append(value[1])

plt.plot(x_mean,y_mean,'ro',label='mean')
plt.plot(x_median,y_median,'go',label='median')

# plt.hist(x_median, bins=np.logspace(0.1, 10, 10000))
# plt.gca().set_xscale("log")

plt.legend(loc='upper left')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('# of following')
plt.ylabel('# of tweets')
plt.show()




# for index, value in enumerate(list(zip(followers,statuses))):
#     if value[1] > 175000:
#         print(value[0])
#
# print(list(zip(followers,statuses)))
# print(pd.DataFrame.groupby([followers,statuses],as_index=False))
# np.log10(statuses)


# idsList = []
# for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/followers'):
#     with open('C:/Users/jyifa/Desktop/Si608/project/followers/' +file) as ids:
#         idsList.append(json.load(ids))
# idsList = list(chain.from_iterable(idsList))
#
# for i in idsList:
#     # print(i)
#     for j in i[1]:
#         print(j)
#         print(j["following_count"])
# # followers = pd.DataFrame(idsList)['followers_count']
# # statuses = pd.DataFrame(idsList)['statuses_count']
# # followers = followers.values
# # statuses= statuses.values

