
import numpy as np

rest_sales = np.loadtxt('Files/Restaurants.txt',delimiter = ',',usecols = (1,2))

print 'The total change in sales for all 5 restaurants is: {}'\
        .format(int(np.ediff1d(rest_sales.sum(0))[0]))