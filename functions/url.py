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

urlList = pd.DataFrame(idsList)['url']
instanceList = {}
for url in urlList:
    try:
        temp = url.split("/")
        instance = temp[2]
        if instance in instanceList:
            instanceList[instance] += 1
        else:
            instanceList[instance] = 1
    except:
        continue

print(instanceList)