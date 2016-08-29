name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

# Create empty dictionary
dict = {}
most_occurences = 0
name = ""
list = [i.split()[1] for i in handle.readlines()
               if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
for i in list:
    if not dict.has_key(i):
        dict[i] = 1
    else:
        dict[i] +=1
        if most_occurences < dict[i]:
            most_occurences = dict[i]
            name = i
print name, most_occurences
