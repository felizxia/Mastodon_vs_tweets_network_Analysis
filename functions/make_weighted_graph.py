# from functions import graph_make
import networkx as nx
import json
import json
import re
import operator
from collections import OrderedDict
from itertools import chain
import networkx as nx
import matplotlib.pyplot as plt

def get_instance_connect():
    instances = open('instances.txt', 'r').read().split()
    uni_dict = {}
    for instance in instances:
        ac_dict = {}
        instance2 = re.compile(r'(https://)(.*?)(/.*)')
        try:
            with open('accounts/' + str(instance)+'/' + 'accounts/accounts.json', 'r') as accounts:
                account_info = json.load(accounts)
                uni_dict[instance] = ac_dict  # change this with file_name--> current instance
                for i in account_info:
                    urls = i['url']
                    url = instance2.search(urls)
                    if url:
                        url = url.group(2)
                        if url in instances:
                            ac_dict[url] = ac_dict.get(url, 0) + 1
        except:
            pass
    with open('instance_connect_correct.json', 'w') as file:
        file.write(json.dumps(uni_dict))

def write_instance_connections():
    with open('instance_connect_correct.json','r') as instance:
        instance= json.load(instance)
        domain= list(instance.keys())
        with open('instance_pairs.txt','w') as pair:
            for i in domain:
                domain_list=instance[i].keys()
                for item in domain_list:
                    instance_connect_1= i
                    instance_connect_2=item
                    pair.write(str(instance_connect_1)+'\t'+str(instance_connect_2))
                    pair.write('\n')

get_instance_connect()
write_instance_connections()
# i_c = nx.read_gml('instance_connection/instance_pairs_new.gml')
# nx.draw_networkx(i_c,with_labels=False)
# plt.show()