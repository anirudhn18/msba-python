#Defining function to get all even numbers first
def even_list(x):
    even_nums = list()
    for i in x:
        if i%2 ==0:
            even_nums.append(i)
    if len(even_nums) == 0:
        even_nums.append(-1)
    return even_nums

def two_digits(x):
    two_digs = list()
    for i in x:
        if len(str(i)) == 2:
            two_digs.append(i)
    return len(two_digs)


def count_odds(x):
    even_nums = even_list(x)
    
    if even_nums == [-1]:
        return len(x)
    else:
        return len(x)-len(even_nums)



nums = [47, 36, 71, 63, 12, 80, 90, 42, 25, 92, 45, 42, 5, 74, 77, 25, 0, 30, 91, 71]

print "The sum is {}".format(sum(nums))

print "The average is {}".format(float(sum(nums))/len(nums))

print "The largest even number is {}".format(max(even_list(nums)))

print "The number of two digit numbers is {}".format(two_digits(nums))

print "The number of odd numbers is {}".format(count_odds(nums))