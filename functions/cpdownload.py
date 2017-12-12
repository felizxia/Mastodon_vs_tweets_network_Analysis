from mastodon import Mastodon
import os
from shutil import copyfile

instances = open('./instances.txt', 'r')

for instance in instances:
    print 'https://' + str.rstrip(instance)
    copyfile('./download.py', str.rstrip(instance) + '/download.py')

