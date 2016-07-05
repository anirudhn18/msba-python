
import numpy as np

store_sales = np.array([[25,64,23,45,14],[12,82,19,34,63],[54,22,17,43,35]])

item_prices = np.array([12,17.95,95,86.5,78])


print 'Sales per store:'
for store in store_sales:
    item_sales = np.array(store)
    print '${:.2f}'.format(np.sum(np.multiply(item_sales,item_prices)))