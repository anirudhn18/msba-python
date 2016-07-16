
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

letter_grades = pd.read_csv('Files/grades.txt',squeeze = True,header = None)

grade_conversion = {
                    'A':4,
                    'A-':3.67,
                    'B+':3.33,
                    'B':3,
                    'B-':2.67,
                    'C+':2.33,
                    'C':2,
                    'C-':1.67,
                    'D+':1.33,
                    'D':1,
                    'F':0
                    }


number_grades = pd.Series([ grade_conversion[letter_grade]\
                for letter_grade in letter_grades ])

# Interpolated median, M - 0.167 + (0.5*N - n1)/n2*0.333

M = np.median(number_grades)
N = len(number_grades)
n1 = len([num_grade for num_grade in number_grades if num_grade < M])
n2 = len([num_grade for num_grade in number_grades if num_grade == M])

int_median = (M - 0.167 + (0.5*N - n1)/n2*0.333)

print 'Interpolated median is {:.2f}'.format(int_median)