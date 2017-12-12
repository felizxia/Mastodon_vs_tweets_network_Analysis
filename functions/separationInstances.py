import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from numpy import cumsum
import json
import os
import fnmatch
from itertools import chain
import csv
from datetime import datetime
import matplotlib.dates as mdates


G = nx.read_gml('user_followers.gml')
# nx.draw_networkx(G, with_labels=True)
print (nx.info(G))


idsList = []
for file in os.listdir('C:/Users/jyifa/Desktop/Si608/project/accounts'):
    with open('C:/Users/jyifa/Desktop/Si608/project/accounts/' +file) as ids:
        idsList.append(json.load(ids))
idsList = list(chain.from_iterable(idsList))

id_list = pd.DataFrame(idsList)['id']
create_time = pd.DataFrame(idsList)['created_at']
url_list = pd.DataFrame(idsList)['url']

# print(len(create_time))
# print(len(id_list))

local_id = []
local_user_create_time = []
for index, url in enumerate(url_list):
    try:
        words = url.split("/")
        instance = words[2]
        if instance == "mastodon.social":
            local_id.append(id_list[index])
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

mpl_data = mdates.date2num(covert_user_create_time)

target_time = mdates.date2num(datetime( 2017, 1, 1, 0, 0))

need_remove_node = []
for node in G.nodes():
    if node not in local_id:
        need_remove_node.append(node)

for index, time in enumerate(mpl_data):
    if time > target_time:
        need_remove_node.append(local_id[index])

for node in need_remove_node:
    try:
        G.remove_node(node)
    except:
        continue


nx.draw(G)
plt.show()
print (nx.info(G))