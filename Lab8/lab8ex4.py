
import numpy as np

degrees_file = np.loadtxt('Files/degrees.txt',delimiter = ',',dtype= str)

degrees = [row[0] for row in degrees_file]
increments = [int(row[2])/float(row[1]) - 1  for row in degrees_file]

order = np.argsort(increments)

#loop to print in descending order
for i in range(0,len(order)):
    index = order[len (order) - i -1 ]
    print '{} {:.2f}%'.format(degrees[index],increments[index]*100)