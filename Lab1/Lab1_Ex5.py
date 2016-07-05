
#Gathering user inputs and doing data type convesions

miles = float(raw_input("Enter miles: "))
yards = float(raw_input("Enter yards: "))
feet = float(raw_input("Enter feet: "))
inches = float(raw_input("Enter inches: "))


#Converting the total distance to inches
dist_in_inches = 63360*miles + 36*yards + 12*feet + inches

dist_in_cm = round(dist_in_inches/0.3937,2)

cm = dist_in_cm%100
#100 centimeters to a meter
m = int((dist_in_cm/100)%1000)
#100000 centimeters to a kilometer
km = int((dist_in_cm/100000)%1000)

#Printing final output
print "The metric length is : \n {0} kilometres \n {1} meters \n {2} centimeters".format(km,m,cm)