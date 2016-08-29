text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('.')
print pos

sppos = text.find('5',pos)
print sppos

result = text[pos-1 :sppos+1]
print result
