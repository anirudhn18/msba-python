

def classify_eggs(eggs) :
    
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
            
egg_weights = [1.21, 1.82, 1.9, 1.31, 2.45, 2.2, 1.4, 2.74, 2.99, 2.38]
eggs = classify_eggs(egg_weights)

for key in eggs:
    print '{}: {}'.format(key,eggs[key])