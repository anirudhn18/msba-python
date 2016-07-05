
denom = int(raw_input("Please enter the maximum denominator: "))
soln = 0

for i in range(1, denom + 1):
    soln += 1/float(i)

print "The sum is {}".format(soln)