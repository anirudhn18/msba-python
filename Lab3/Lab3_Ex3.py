
def sumavg(input_list):
    sum_out = sum(input_list)
    avg_out = float(sum(input_list))/len(input_list)
    return sum_out,avg_out

user_sum, user_avg = sumavg([1,2,3])

print 'The total is {} and the average is {}.'.format(user_sum, user_avg)