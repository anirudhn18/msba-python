

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def vowel_count(name):
    count = 0
    if name.find('a') >= 0:
        count += 1
    if name.find('e') >= 0:
        count += 1
    if name.find('i') >= 0:
        count += 1
    if name.find('o') >= 0:
        count += 1
    if name.find('u') >= 0:
        count += 1
    
    return count

us_states = pd.read_csv('Files/USStates.txt', header = None, \
                        names = ['State Name','Code','Area','Population'])


print 'Total population of the US is {}'.format(us_states['Population'].sum())

print 'Total area of the US is {}'.format(us_states['Area'].sum())

print 'Population density of the US is {}'.\
        format(us_states['Population'].sum()/float(us_states['Area'].sum()))

print 'State(s) with longest name:'
max_len = max(us_states['State Name'].map(len))
maxlen_states = [state for state in us_states['State Name'] \
                if len(state) == max_len] 
print maxlen_states


print 'States with 4 of 5 vowels:'

vowel_states = [state for state in us_states['State Name']\
                if vowel_count(state.lower())>3]
                    
print vowel_states