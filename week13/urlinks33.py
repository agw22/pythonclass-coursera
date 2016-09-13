import urllib
from BeautifulSoup import *


url = raw_input('Enter URL : ')
position = raw_input('Enter position : ')
count = raw_input('Enter count : ')

urlhandle = urllib.urlopen(url)
data = urlhandle.read()
soup = BeautifulSoup(data)
tags = soup('a')
links = list()

for tag in tags:
    links.append(tag.get('href', None))

print 'Retrieving: ', links[0]
print 'Retrieving: ', links[int(position)-1]

link = links[int(position)-1]
counter = 1
while counter < int(count):
    urlhandle = urllib.urlopen(link)
    data = urlhandle.read()
    soup = BeautifulSoup(data)
    tags = soup('a')
    links = list()

    for tag in tags:
        links.append(tag.get('href', None))
    print 'Retrieving: ', links[int(position)-1]
    link = links[int(position)-1]
    counter = counter + 1
