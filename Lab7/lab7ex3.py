
import numpy as np
import timeit as tt
import math as m
import random

#log function for unary
def log(np_array):
    result_list = list()
    for num in np_array:
        result_list.append(m.log(num))
    return np.array(result_list)


#modulo function for binary
def modulo(np_array1,np_array2):
    result_list = list()
    for index in range(0,len(np_array1)):
        result_list.append(np_array1[index]%np_array2[index])
    
    return np.array(result_list)


nums = list(np.floor(100*(np.random.rand(5000))) + 1)
more_nums = list(np.floor(100*(np.random.rand(5000))) + 1)


#Unary operator comparison
print 'Comparison of np.log:'
time_nplog = tt.timeit('np.log(np.array({}))'.format(nums),\
                        'import numpy as np',number= 100000)

time_mylog = tt.timeit('log({})'.format(nums),\
                        'from __main__ import log',number= 100000)
                        
if time_nplog < time_mylog :
    pct = (time_mylog - time_nplog) / time_nplog
    print 'Numpy method is {:.1f}% faster.'.format(pct * 100)
else:
    pct = (time_nplog - time_mylog ) / time_mylog 
    print 'Looping method is is {:.1f}% faster.'.format(pct * 100)



#Binary operator comparison
print 'Comparison of np.mod:'
time_npmod = tt.timeit('np.mod(np.array({}),np.array({}))'.format(nums,more_nums),\
                        'import numpy as np',number= 100000)

time_mymod = tt.timeit('modulo({},{})'.format(nums,more_nums),\
                        'from __main__ import modulo',number= 100000)


if time_npmod < time_mymod :
    pct = (time_mymod - time_npmod) / time_npmod
    print 'Numpy method is {:.1f}% faster.'.format(pct * 100)
else:
    pct = (time_npmod - time_mymod ) / time_mymod 
    print 'Looping method is is {:.1f}% faster.'.format(pct * 100)
    
    
    

#Results of the comparitive test:

#Comparison of np.log:
#Numpy method is 481.6% faster.
#Comparison of np.mod:
#Numpy method is 108.3% faster.