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


def follow_relationship_write(file):
    following_net = open(str(file)+str('.txt'), 'w')
    dict = {}
    for file in os.listdir('/Users/rita/Google Drive/608/network/following/'): # change path
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

follow_relationship_write('followings')
follow_relationship_write('followers')

# load followers and following file; write graph function
def write_graph(file):
    fol = nx.DiGraph()
    with open(str(file)+str('.txt'))as follow:
        for line in follow:
            follower = line.strip().split('\t')
            follower = (follower[0],follower[1])
            fol.add_edge(*follower)
    nx.write_gml(fol,str(file) + ".gml")
    return fol

write_graph("user_followings")
write_graph("user_followers")

## read graph file, print basic information
followers= nx.read_gml("user_followers.gml")
followings= nx.read_gml("user_followings.gml")
# print (nx.info(followers))
# print (nx.info(followings))


# random pick a node, calculate shortest path length
def degree_separate(file):
    from random import sample
    import json
    import matplotlib.pylab as plt
    import numpy as np
    sample_n1=1000
    sample_n2 =3000
    sample_n3 =8000
    source_list_one = sample(file.nodes(),sample_n1)
    source_list_two = sample(file.nodes(),sample_n2)
    source_list_three = sample(file.nodes(),sample_n3)
    sample_1000 = open('sample_on_1000_nodes_following.csv','w') # you can save it or not
    sample_3000 = open('sample_on_3000_nodes_following.csv','w')
    sample_8000 = open('sample_on_8000_nodes_following.csv','w')
    counts_path_1=dict()
    counts_path_2=dict()
    counts_path_3=dict()
    for time in range(3):
        time += 1
        if time==1:
            for i in source_list_one:
                sample_1000.write(str(i)+"\t")
                dictone=nx.single_source_shortest_path_length(file,source=i)
                path_valuesone = list(dictone.values())
                for item in path_valuesone:
                    counts_path_1[item] = counts_path_1.get(item,0)+1
        if time==2:
            for i in source_list_two:
                sample_3000.write(str(i) + "\t")
                dictwo = nx.single_source_shortest_path_length(file, source=i)
                path_valuestwo = list(dictwo.values())
                for item in path_valuestwo:
                    counts_path_2[item] = counts_path_2.get(item, 0) + 1
        if time==3:
            for i in source_list_three:
                sample_8000.write(str(i)+"\t")
                dicthree = nx.single_source_shortest_path_length(file, source=i)
                path_valuesthree = list(dicthree.values())
                for item in path_valuesthree:
                    counts_path_3[item] = counts_path_3.get(item, 0) + 1
    print(counts_path_1) # check path dictionary
    print(counts_path_2)
    print(counts_path_3)
    r1, g1, b1 = np.random.uniform(0, 1, 3)
    r2, g2, b2 = np.random.uniform(0, 1, 3)
    r3, g3, b3 = np.random.uniform(0, 1, 3)
    x1,y1 = zip(*counts_path_1.items())
    x2,y2 = zip(*counts_path_2.items())
    x3,y3= zip(*counts_path_3.items())
    y1= tuple(v/sum(y1)for v in y1)
    y2= tuple(v/sum(y2)for v in y2)
    y3= tuple(v/sum(y3)for v in y3)
    plt.plot(x1,y1,'ks-',markevery=range(len(x1)),markersize=5, markerfacecolor='none',markeredgewidth=1.5,markeredgecolor=(r1, g1, b1 ,1))
    plt.plot(x2,y2,'ks-',markevery=range(len(x2)),markersize=5, markerfacecolor='none',markeredgewidth=1.5,markeredgecolor=(r2, g2, b2 ,1))
    plt.plot(x3,y3,'ks-',markevery=range(len(x3)),markersize=5, markerfacecolor='none',markeredgewidth=1.5,markeredgecolor=(r3, g3, b3,1))
    plt.legend(['1000 sample', '3000 sample', '8000 sample'], loc='upper right')
    plt.ylabel('probability')
    plt.xlabel('Distance from the seed')
    plt.title('Degree of separation')
    plt.show()
    plt.savefig('degree_of_separation_'+str(file)+'.png')

degree_separate(followers)
degree_separate(followings)
# cdf distribution of graphs

def degree_separation_cdf(file):
    if file =="user_followings":
        dict_fl = defaultdict(int)
        for i in list(followings.out_degree().values()):
            dict_fl[i] += 1
        items=sorted(dict_fl.items(),reverse=True)
        x,y = np.array(items).T
        y = [float(i)/sum(y) for i in y]
        y = cumsum(y)
        plt.plot(x, y, 'bo')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(['in_Degree'])
        plt.xlabel('$K$', fontsize=20)
        plt.ylabel('$P_K$', fontsize=20)
        plt.title('$Degree\,Distribution\,of\,Followers$', fontsize=20)
        plt.show()
    if file=="user_followers":
        dict_fr = defaultdict(int)
        for i in list(followers.in_degree().values()):
            dict_fr[i] += 1
        for i in list(followers.in_degree().values()):
            dict_fr[i]+=1
        items=sorted(dict_fr.items(),reverse=True)
        x,y = np.array(items).T
        y = [float(i)/sum(y) for i in y]
        y = cumsum(y)
        plt.plot(x, y, 'bo')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(['in_Degree'])
        plt.xlabel('$K$', fontsize=20)
        plt.ylabel('$P_K$', fontsize=20)
        plt.title('$Degree\,Distribution\,of\,Followers$', fontsize=20)
        plt.show()
degree_separation_cdf("user_followings")
degree_separation_cdf("user_followers")
