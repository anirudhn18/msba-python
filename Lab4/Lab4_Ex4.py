

import timeit as tt

def list_method(filename):
    with open(filename,'r') as f:
        list_f = list(f)
    return list_f       
    
    
def readline_method(filename):

    with open(filename,'r') as f:
        list_f = f.readlines()
    return list_f
    
    
def loop_method(filename):
    list_f = list()
    with open(filename,'r') as f:
        for line in f:
            list_f.append(line)
    return list_f
    


file_name = 'chinese.csv'

list_time = tt.timeit('list_method("{}")'.format(file_name),\
'from __main__ import list_method', number = 100000)

readline_time = tt.timeit('readline_method("{}")'.format(file_name),\
'from __main__ import readline_method', number = 100000)

loop_time = tt.timeit('loop_method("{}")'.format(file_name),\
'from __main__ import loop_method', number = 100000)


times = {loop_time:'Looping method',list_time:'List(f) method',\
readline_time:'f.readline() method'}

ordered = sorted(times)

print "{} is faster than {} by {:.2f}%".format( times[ordered[0]], times[ordered[1]],\
 abs(ordered[1]/ordered[0] - 1)*100 )

print "{} is faster than {} by {:.2f}%".format( times[ordered[0]], times[ordered[2]],\
 abs(ordered[2]/ordered[0] - 1)*100 )
