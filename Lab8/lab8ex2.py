

import numpy as np
import timeit as tt
import math as m

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

time_nplog = tt.timeit('np.log(np.array({}))'.format(nums),\
                        'import numpy as np',number= 100000)

time_mylog = tt.timeit('log({})'.format(nums),\
                        'from __main__ import log',number= 100000)

time_lclog = tt.timeit('[m.log(num) for num in {}]'.format(nums),\
               'import math as m', number=100000)



unary_times = {time_nplog:'Numpy',time_mylog:'Custom function',\
                time_lclog:'List Comprehension'}

sorted_unary = sorted(unary_times)


print 'For the unary comparison,'

print '{} is the fastest !'.format(unary_times[sorted_unary[0]])
print 'Faster than {} by {:.2f}%'.\
format(unary_times[sorted_unary[1]], 100*(sorted_unary[1]/sorted_unary[0] - 1))
print 'Faster than {} by {:.2f}%'.\
format(unary_times[sorted_unary[2]], 100*(sorted_unary[2]/sorted_unary[0] - 1))


#For the unary comparison,
#Numpy is the fastest !
#Faster than List Comprehension by 268.11%
#Faster than Custom function by 469.91%


                        

#Binary operator comparison
print 'Comparison of np.mod:'
time_npmod = tt.timeit('np.mod(np.array({}),np.array({}))'.format(nums,more_nums),\
                        'import numpy as np',number= 100000)

time_mymod = tt.timeit('modulo({},{})'.format(nums,more_nums),\
                        'from __main__ import modulo',number= 100000)

time_lcmod = tt.timeit('[num1%num2 for num1,num2 in zip({},{})]'.\
                        format(nums,more_nums),number = 100000)


binary_times = {time_npmod:'Numpy',time_mymod:'Custom function',\
                time_lcmod:'List Comprehension'}


sorted_binary = sorted(binary_times)

print 'For the binary comparison,'

print '{} is the fastest !'.format(binary_times[sorted_binary[0]])
print 'Faster than {} by {:.2f}%'.\
format(binary_times[sorted_binary[1]],100*(sorted_binary[1]/sorted_binary[0] - 1))
print 'Faster than {} by {:.2f}%'.\
format(binary_times[sorted_binary[2]],100*(sorted_binary[2]/sorted_binary[0] - 1))

#For the binary comparison,
#Numpy is the fastest !
#Faster than List Comprehension by 43.20%
#Faster than Custom function by 103.23%
    



