
#Prompting inputs and performing data type conversions

cust_name = raw_input("Please enter customer name: ")

labor_hours = float(raw_input("Please enter labor hours: "))

parts_cost = float(raw_input("Please enter cost of parts and supplies: "))



#Calculating labor cost and parts cost after taxes
labor_cost = labor_hours*35
total_parts_cost = 1.07*parts_cost

#Calculating total cost
total_cost = labor_cost + total_parts_cost


#Printing the bill
print "Customer: " + cust_name
print "Labor cost: {0}".format(round(labor_cost,2))
print "Parts cost: {0}".format(round(total_parts_cost,2))
print "Total cost: {0}".format(round(total_cost,2))