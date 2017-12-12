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

instances = open('./instances.txt', 'r')
i = 0


def degree_separate(file):
    from random import sample
    import json
    import matplotlib.pylab as plt
    import numpy as np
    if len(file.nodes()) < 5000:
        sample_n3 = len(file.nodes())
    else:
        sample_n3 = 5000
    source_list_three = sample(file.nodes(),sample_n3)
    #sample_8000 = open('sample_on_8000_nodes_following.csv','w')
    counts_path_3=dict()
    for i in source_list_three:
        #sample_8000.write(str(i)+"\t")
        dicthree = nx.single_source_shortest_path_length(file, source=i)
        path_valuesthree = list(dicthree.values())
        for item in path_valuesthree:
            counts_path_3[item] = counts_path_3.get(item, 0) + 1
    #print(counts_path_3)
    r3, g3, b3 = np.random.uniform(0, 1, 3)
    x3,y3= zip(*counts_path_3.items())

    #y3= tuple((0.0+v)/sum(y3) for v in y3)

    return sum([0.0+i*y3[i] for i in range(1, len(y3))])/sum(y3)



df = pd.DataFrame(columns=['instance','degree','separation','Diameter','Components','Density','Average Degree'])
for instance in instances:
    print instance
    if str.rstrip(instance) != 'vocalodon.net':
        followings= nx.read_gml('C:/Users/esbra/OneDrive/Mastodon/' + str.rstrip(instance) +'/following/following.gml')
        if len(followings.nodes()) > 0:
            gdegree = degree_separate(followings)
            ndegree = len(nx.nodes(followings))
            followings = nx.read_gml('C:/Users/esbra/OneDrive/Mastodon/'+ str.rstrip(instance) +'/following/following.gml')
            gdiameter = nx.diameter(max(nx.strongly_connected_component_subgraphs(followings), key=len))
            gsubcomps = sum(1 for _ in nx.weakly_connected_component_subgraphs(followings))
            gdensity = nx.density(followings)
            goutdegree = np.mean(followings.out_degree().values())
            df.loc[i] = [str.rstrip(instance),ndegree,gdegree,gdiameter,gsubcomps,gdensity,goutdegree]
    print i
    print df
    df.to_csv('C:/Users/esbra/OneDrive/dataframe.csv')
    i = i + 1
    # print sepList
    # with open('C:/Users/esbra/OneDrive/Mastodon/sepList.json','w') as file:
        # json.dump(sepList, file)

# with open('sepList.json') as ids:
    # allIds = json.load(ids)

# #print len(allIds)

# ifile  = open('sepList.csv', "rb")
# reader = csv.reader(ifile)
# ofile  = open('sepList.csv', "wb")
# writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
 
# for row in allIds:
    # writer.writerow([row.keys(), row.values()])
 
# ifile.close()
# ofile.close()
