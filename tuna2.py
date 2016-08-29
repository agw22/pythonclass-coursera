import re

total = 0

file = open('regex_sum_283431.txt', 'r')
mylist = list()
for line in file:
    integers = re.findall('[0-9]+',line)
    #print type(integers)
    if not integers:
        continue
    else:
        for i in integers:
            #print i
            #num = int(i)
            #print type(num)
            mylist.append(int(i))
print sum(mylist)
            #print type(integer)
            #intlist = [int(integer) for integer in integers]
            #print intlist
            #list = [int(integer)]
            #print type(list)
            #for items in list:
            #    print items
                #sum = sum + items
                #print sum
            #list = []
            #converted = int(integer)
            #for i in converted:
            #    list[i] += 1
            #    print list
            #print type(converted)
            #for i in converted:
            #    sum = sum + i
            #    print sum
