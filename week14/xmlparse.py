import urllib
import xml.etree.ElementTree as ET

serviceurl = raw_input('Enter location: ')
if len(serviceurl) < 1 : quit()

url = urllib.urlopen(serviceurl)
data = url.read()
print data
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print 'Number of commentors:', len(results)
commentsum = 0
for comment in results:
    commentsum = commentsum + int(comment.find('count').text)
print 'Sum:', commentsum
