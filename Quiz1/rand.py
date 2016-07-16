my_list = []
for i in range(0,50):
    my_list.append(i)
my_list[34] = 51


my_list[34] 


def foo(a,b):
    return a*b + 2

def bar(b,c):
    tot = 0
    for i in range(b,c):
        tot += i
    
    return tot

foo(3,1)*bar(1,7)






class point:
    """ggg"""
    
a = point()

b = point()

a.x = 10

b = a

a.x = 20
b.x

a = ['Ani','gg','wp']



for word in a:
    if a.index(word)%2 == 0 :
        print word
        

for a_nation in nations:
    density = a_nation.pop / a_nation.area
    print '{} has a density of {:.2f}'.format(a_nation.name,density)
    
i = 0 
asd
while i < len(nations):
    nation = nations[i]
    density = nation.pop/nation.area
    print '{} has a density of {:.2f}'.format(nation.name,density)
    i += 1
    
    
while number > 1:
    number /= 2
    
nums = [1, 0, 8, 7, 6]

for a_number in nums:
    print employees[a_number].id


i = 0

while i < len(nums):
    employee = employees[i]
    print employee.id
    i+ = 1
    
for a_student in range(len(names)):
    student_scores = list()
    for score in scores[a_student]:
        student_scores.append(score)
    print '{}: {:.1f}'.format(names[a_student],median(student_scores))


