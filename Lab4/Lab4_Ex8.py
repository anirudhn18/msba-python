
#Improving the counting eggs 
import timeit as tt

def classify_eggs_old(eggs) :
    
    egg_grades = list()
    for egg_wt in eggs :      
        if egg_wt >= 1.5 and egg_wt < 1.75:
            egg_grades.append('Small')
        elif egg_wt >= 1.75 and egg_wt < 2:
            egg_grades.append('Medium')
        elif egg_wt >= 2 and egg_wt < 2.25:
            egg_grades.append('Large')
        elif egg_wt >= 2.25 and egg_wt < 2.5:
            egg_grades.append('Extra Large')
        elif egg_wt >= 2.5:
            egg_grades.append('Jumbo')
        else:
            egg_grades.append('X')
    
    grade_count = dict()    
    for grade in egg_grades:
        if grade != 'X':
            grade_count[grade] = grade_count.get(grade,0)  + 1

    return grade_count
    

def classify_eggs_new(eggs) :
    
    grade_count = dict()    
    for egg_wt in eggs:
        if egg_wt >= 2.5:
            grade_count['Jumbo'] = grade_count.get('Jumbo',0) + 1
        elif egg_wt >= 2.25:
            grade_count['Extra Large'] = grade_count.get('Extra Large',0) + 1
        elif egg_wt >= 2:
            grade_count['Large'] = grade_count.get('Large',0) + 1
        elif egg_wt >= 1.75:
            grade_count['Medium'] = grade_count.get('Medium',0) + 1
        elif egg_wt >= 1.5:
            grade_count['Small'] = grade_count.get('Small',0) + 1
            
    return grade_count


egg_weights = [1.21, 1.82, 1.9, 1.31, 2.45, 2.2, 1.4, 2.74, 2.99, 2.38]


old_time = tt.timeit('classify_eggs_old({})'.format(egg_weights),\
'from __main__ import classify_eggs_old', number = 1000000)


new_time = tt.timeit('classify_eggs_new({})'.format(egg_weights),\
'from __main__ import classify_eggs_new', number = 1000000)


if old_time > new_time:
    print "Timing improved by {:.2f}%".format((1 - new_time/old_time)*100)
else:
    print "No improvement in runtime"
    
    
    
# 1. There is a 50% improvement in timing when run using the new code
# 
# 2. The new code does not involve creation of a list of egg sizes 
#     before the sizes are counted. 
#     This lack of steps uses up lesser memory and speeds up the code runtime
#     
# 3. The new code is also shorter by 7 ( 12 from 19 ), 
#     which makes it better from a maintainance point of view. 
#     It also uses lesser variables and objects. 