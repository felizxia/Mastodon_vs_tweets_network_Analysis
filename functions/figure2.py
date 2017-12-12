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
for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/accounts'):
    with open('C:/Users/jyifa/Desktop/Si608/project/accounts/' +file) as ids:
        idsList.append(json.load(ids))
idsList = list(chain.from_iterable(idsList))

followers = pd.DataFrame(idsList)['followers_count']
statuses = pd.DataFrame(idsList)[['followers_count','statuses_count']]

unique = {}
for i in followers:
    if i not in unique:
        unique[i] = 1
    else:
        unique[i] += 1
print(unique)

followers_statuses_mean = statuses.groupby(statuses['followers_count'],as_index=False).mean()
followers_statuses_median = statuses.groupby(statuses['followers_count'],as_index=False).median()

x_median = []
y_median = []
for value in followers_statuses_median.values:
    x_median.append(value[0])
    y_median.append(value[1])


x_mean = []
y_mean = []
for value in followers_statuses_mean.values:
    x_mean.append(value[0])
    y_mean.append(value[1])

# x_line = []
# y_line = []
# new_x_median = np.log10(x_median)
# new_index = 1
# prev = 0
# for i in np.linspace(0.0, 4.0, num=60):
#     y_sum = 0
#     count = 0
#     while new_x_median[new_index] < i:
#         count += 1
#         y_sum += y_median[new_index]
#         new_index += 1
#     if count != 0:
#         x_line.append(10**i)
#         y_line.append(y_sum/count)
# plt.plot(x_line,y_line,'b',label='line')


plt.plot(x_mean,y_mean,'ro',label='mean')
plt.plot(x_median,y_median,'go',label='median')

plt.legend(loc='upper left')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('# of followers')
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

