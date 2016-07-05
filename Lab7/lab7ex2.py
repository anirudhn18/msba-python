
import numpy as np
import csv

ranking_list = list()

with open('Ranking.txt','r') as f:
    for row in csv.reader(f):
        ranking_list.append(row)
        
ranking_arr = np.array(ranking_list,dtype = str)

print ranking_arr



uni = raw_input('University Name: ')

print '{} is highly ranked in:'.format(uni)

majors = list()
for major in ranking_arr:
    if uni in major[1:]:
        majors.append(major[0])

if len(majors) == 0:
    print '{} does not appear in the rankings.'.format(uni)
else :
    for each in majors:
        print each