import re

file = open('regex_sum_283431.txt', 'r')
mylist = list()
for line in file:
    integers = re.findall('[0-9]+',line)
    if not integers:
        continue
    else:
        for i in integers:
            mylist.append(int(i))
print sum(mylist)
