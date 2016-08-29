fname = raw_input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
list = [i.split() for i in fh.readlines()
               if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
for i in list:
    print i[1]
    count += 1
print "There were", count, "lines in the file with From as the first word"
