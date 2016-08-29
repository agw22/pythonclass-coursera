largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        number = int(num)
        largest = num if largest < num or largest == None else largest
        smallest = num if smallest > num or smallest == None else smallest
    except:
        print "Error please enter numeric input"
        quit

print "Maximum number is", largest
print "Minumum number is", smallest
