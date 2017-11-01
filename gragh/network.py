# write file number ahead the userid: followers

import json
import os
import fnmatch
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# debugging

        # user_id=i[0]
        # print (user_id)
        # print (len(i[1]))

following_net = open('following.txt', 'w')
dict = {}
for file in os.listdir('/Users/rita/Google Drive/608/network/following/'):
    root, ext = os.path.splitext(file)
    if ext == '.json':
        with open(str('/Users/rita/Google Drive/608/network/following/' + file)) as follow:
            following = json.load(follow)
            for i in following:
                user_id = i[0]
                for j in i:
                    if type(j) is list:
                        for k in j:
                            fol = k.get('id')
                            dict[user_id] = fol
                            following_net.write(str(user_id) + '\t' + str(fol))
                            following_net.write('\n')

print (len(list(dict.keys())))
print (len(list(dict.values())))

follower_net = open('followers.txt', 'w')
dict = {}
for file in os.listdir('/Users/rita/Google Drive/608/network/followers/'):
    root, ext = os.path.splitext(file)
    if ext == '.json':
        with open(str('/Users/rita/Google Drive/608/network/followers/' + file)) as follower:
            follow = json.load(follower)
            for i in follow:
                user_id = i[0]
                for j in i:
                    if type(j) is list:
                        for k in j:
                            fol = k.get('id')
                            dict[user_id] = fol
                            follower_net.write(str(user_id) + '\t' + str(fol))
                            follower_net.write('\n')

print (len(list(dict.keys())))
print (len(list(dict.values())))

