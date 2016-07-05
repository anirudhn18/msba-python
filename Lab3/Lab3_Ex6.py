
def is_sorted(state_list):
    
    state_sorted = sorted(state_list)
    
    for state in state_list:
        if state_list.index(state) != state_sorted.index(state) :
            return False
            break
    else:
        return True
        
        

states = ['Connecticut',
 'Delaware', 
 'Georgia',
 'Maryland',
 'Massachusetts',
 'New Hampshire',
  'New York',
 'New Jersey',

 'North Carolina',
 'Pennsylvania',
 'Rhode Island',
 'South Carolina',
 'Virginia']

print states
print sorted(states)


if is_sorted(states):
    print 'The list is sorted.'
else:
    print 'The list is not sorted.'