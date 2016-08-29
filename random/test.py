def computepay(h,r):
    hours = float(h)
    rate = float(r)
    if hours > 40:
        othr = (hours - 40)
        ot = float(othr)
        pay = (40 * rate) + (ot * 15.75)
    elif h <= 40:
        pay = (hours * rate)
    return pay

h = raw_input("Enter Hours:")
r = raw_input("Enter Rate of Pay:")
p = computepay(h,r)
print "Pay",p
