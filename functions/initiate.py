import os
import json
from itertools import chain

instances = open('./instances.txt', 'r')


def consolidate(instance, type):
    idsList = []
    pathTo = 'C:/Users/esbra/OneDrive/Mastodon/' + str.rstrip(instance) + '/'
    for file in os.listdir(pathTo + type + '/'):
        with open(pathTo + type + '/' + file) as ids:
            idsList.append(json.load(ids))
        if file == type + '.json':
            idsList = list(chain.from_iterable(idsList))
        if file != type + '.json':
            os.remove(pathTo +  type + '/' + file)
    with open(pathTo + type + '/' + type + '.json', 'w') as typeFile:
        json.dump(idsList, typeFile)  

for instance in instances:
    print 'https://' + str.rstrip(instance)
    consolidate(instance, 'accounts')
    consolidate(instance, 'followers')
    consolidate(instance, 'following')

