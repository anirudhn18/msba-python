
import numpy as np
import csv

miles_between = np.empty([4,4],dtype = np.int32)

with open('Distances.txt','r') as f:
    count = 0
    for row in csv.reader(f):
        miles_between[count] = row
        count += 1
miles_between


print 'Cities:'
print '1 Chicago'
print '2 Los Angeles'
print '3 New York'
print '4 Philadelphia'

origin = int(raw_input('Please enter origin city: '))
dest = int(raw_input('Please enter destination city: '))

distance = miles_between[origin-1,dest-1]

print 'The distance between cities is: {}'.format(distance)