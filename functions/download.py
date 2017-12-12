from mastodon import Mastodon
import time
import json
import datetime
import os
from itertools import chain



folder = str(os.path.dirname(os.path.realpath(__file__))).split('\\')[-1]
pathTo = 'E:/Mastodon/' + folder + '/'
url = 'https://' + folder

t = 0
while t!=1:
    try:
        Mastodon.create_app(
            'SI608Proj',
            api_base_url = url,
            to_file = '8ea4c1d507d12801f98ab29de09cb1b07cfe2491f4e40b27a433a19e206c41fa')
        t=1
    except:
        time.sleep(120)
        pass


mastodon = Mastodon(
    client_id = '8ea4c1d507d12801f98ab29de09cb1b07cfe2491f4e40b27a433a19e206c41fa',
    access_token = '12408fd6f8e4662f18c87dcf45851fbdaf845a7d6fa9935c41851b37facd6a6c',
    api_base_url = url
)

mastodon.log_in(
    'mastodonanalysis@gmail.com',
    'zjgvyH32MOK3'
)

def datetimeconvert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def getLists(getType):
    listsPage = mastodon.fetch_remaining(getType)
    return j,listsPage

def consolidate(type):
    idsList = []
    for file in os.listdir(pathTo + type + '/'):
        with open(pathTo + type + '/' + file) as ids:
            idsList.append(json.load(ids))
        if file == type + '.json':
            idsList = list(chain.from_iterable(idsList))
        if file != type + '.json':
            os.remove(pathTo +  type + '/' + file)
    with open(pathTo + type + '/' + type + '.json', 'w') as typeFile:
        json.dump(idsList, typeFile)  

allIds = 1

if os.path.isfile(pathTo + 'accounts/accounts.json'):
    with open(pathTo + 'accounts/accounts.json') as ids:
        allIds = json.load(ids)[-1]['id']

j = int(allIds)
t = 0

while j!=10000000 and t!=300:
    accounts = []
    followers = []
    following = []
    error = []
    #print j
    if j % 100 == 0:
        consolidate('accounts')
        consolidate('followers')
        consolidate('following')
   
    try:
        account = mastodon.account(j)
        accounts.append(account)
        with open(pathTo + 'accounts/accounts' + str(j) + '.json', 'w') as accountsFile:
            json.dump(account, accountsFile, default = datetimeconvert)

        if account['url'][:len(url)] == url:
            if len(account) > 0:
                if account["followers_count"] > 0:
                    followersTemp = getLists(mastodon.account_followers(j))
                    if account["followers_count"] != len(followersTemp[1]):
                        error.append(['followers', j])
                    followers.append(followersTemp)

                if account["following_count"] > 0:
                    followingTemp = getLists(mastodon.account_following(j))
                    if account["following_count"] != len(followingTemp[1]):
                        error.append(['followiong',j])
                    following.append(followingTemp)
                with open(pathTo + 'followers/followers' + str(j) + '.json', 'w') as followersFile:
                    json.dump(followers, followersFile, default = datetimeconvert)
                with open(pathTo + 'following/following' + str(j) + '.json', 'w') as followingFile:
                    json.dump(following, followingFile, default = datetimeconvert)                    
        j+=1
    except Exception, e:
        #print folder, str(e)
        if str(e) == "Mastodon API returned error: Throttled":
            t = 0
            time.sleep(120)
        else:
            time.sleep(10)
            j+=1
            t+=1
        pass
    
open(pathTo + 'finished.txt', 'a').close()    
   


    
