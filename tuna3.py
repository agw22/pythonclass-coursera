import re

fname=raw_input('regex_sum_283431.txt')
fh=open(fname, 'r')
y=list()
count=0

    for line in fh:
        y=re.findall('[0-9]+', line)
        inp=list(y)
        if y == []:
            continue
        count= count += sum([int(i) for i in y])
print count
