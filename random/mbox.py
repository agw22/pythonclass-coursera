# Use the file name mbox-short.txt as the file name
try:
    fname = raw_input("Enter file name: ")
    if len(fname) == 0:
        fname = 'mbox-short.txt'
except:
    print "mbox-short.txt please"
    quit

fh = open(fname)
spamcount = 0
spamtotal = 0
answer = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    spamcount = spamcount + 1
    num = float(line[21:])
    spamtotal = num + spamtotal
answer = spamtotal / spamcount
print "Avg spam confidence:", answer
