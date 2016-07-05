import csv

state_with_judges = []

with open('Justices.txt','r') as f1:
    for row in csv.reader(f1):
        if row[3] not in state_with_judges:
            state_with_judges.append(row[3])

with open('USStates.txt','r') as f2:
    for row in csv.reader(f2):
        if row[1] not in state_with_judges:
            print row[0]

