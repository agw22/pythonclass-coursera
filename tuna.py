name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()
for x in handle:
    if x .startswith("From") and len (x.split()) > 2:
        list = x.split()
        if not dic.has.key(1[5][:2])
        dic[1[5][:2]]=1
    else:
        dic[1[5][:2]]+=1

key = sorted(dic)
for x in key:
    print "%s %d" % (x,dic[x])
