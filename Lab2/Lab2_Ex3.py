
hrs = float(raw_input("Please enter the number of hours worked: "))

wage = float(raw_input("Please enter the hourly wage: "))

if hrs > 40:
    pay = 40*wage + (hrs - 40)*(wage*1.5)
else:
    pay = hrs*wage

print "Gross pay is ${:.2f}".format(pay)