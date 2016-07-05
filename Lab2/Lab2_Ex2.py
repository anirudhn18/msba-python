a = 1001

b = int(raw_input("Please enter a whole number between 1 and 1000, or -1 to quit: "))

if b == -1:
    print "You didnt enter any numbers!"
else:
    while b != -1:
        if not (b>0 and b<1001):
            print "Stick to between 1 and 1000, please!!"
        else:
            if b < a: 
                a=b
        b = int(raw_input("Please enter a whole number between 1 and 1000, or -1 to quit: "))
    print "The least so far is {}".format(a)