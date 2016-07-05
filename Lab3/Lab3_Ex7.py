
import numpy as np

#Function definitions

#Function to get number grade from letter grade
def get_nbr_grade(let_grade):

    letter = let_grade[0]
    
    if letter == 'A':
        base = 4
    elif letter == 'B':
        base = 3
    elif letter == 'C':
        base = 2
    elif letter == 'D':
        base = 1
    else :
        base = 0
    
    if len(let_grade)>1 and let_grade[1] == '+':
        sign = 0.33
    elif len(let_grade)>1 and let_grade[1] == '-':
        sign = -0.33    
    else :
        sign = 0
        
    return (base + sign)


#Function to get interpolated median from a list of numbers
def get_int_median(numlist):
    
    M = np.median(numlist)
    N = len(numlist)
    n1,n2 = 0,0
    
    for num in numlist:
        if num < M:
            n1 += 1
        elif num == M:
            n2 += 1
    
    return (M - 0.167 + (0.5*N - n1)/n2*0.333 )

#Main program
grades = ['A-', 'B', 'C', 'A', 'C', 'A', 'B', 'C-', 'C+', 'B-', 'B-', 'A-', 'B', 
'B+', 'C-', 'C+', 'C', 'B-', 'A', 'C', 'C', 'B-', 'A', 'C-', 'C']

nbr_grades = list()

for grade in grades:
    nbr_grades.append(get_nbr_grade(grade))

int_median = get_int_median(nbr_grades)

print "The interpolated median is {:.2f}".format(int_median)

if int_median >= 3.13 and int_median <=3.53 : 
    print "The course is in compliance with the policy"
else :
    print "The course is not in compliance with the policy"