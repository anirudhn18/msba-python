
import numpy as np

prev_sales_list = list()
curr_sales_list = list()

with open('Files/Restaurants.txt','r') as f:
    for row in csv.reader(f):
        prev_sales_list.append(int(row[1]))
        curr_sales_list.append(int(row[2]))
 

prev_yr_sales = np.array(prev_sales_list)
curr_yr_sales = np.array(curr_sales_list)


print 'The total change in sales for all 5 restaurants is: {}'.\
        format(np.sum(np.subtract(curr_yr_sales,prev_yr_sales)))