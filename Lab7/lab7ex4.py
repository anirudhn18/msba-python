
import numpy as np

inventory = np.array([[25,64,23],[30,82,19]])

sales = np.array([[7,45,11],[4,24,8]])

remaining = np.subtract(inventory,sales)

print "Ending inventory:"
print '  1  2  3'

for store in range(0,2):
    print '{}'.format(store+1),
    for item in range(0,3):
        if item != 2:
            print '{}'.format(remaining[store,item]),
        else :
            print '{}'.format(remaining[store,item])