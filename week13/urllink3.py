import urllib
from BeautifulSoup import *

url = raw_input('Enter -')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
numberlist = list()
total = 0

tags = soup('span')
for tag in tags:
    numberlist.append(int(tag.contents[0]))

for val in numberlist:
    total = total + val

print 'Count', len(numberlist)
print 'Sum', total
