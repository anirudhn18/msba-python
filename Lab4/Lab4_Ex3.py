
import csv

potus_n_judges = dict()

with open('Justices.txt') as f:
    for line in csv.reader(f):
        potus = line[2].lower()
        
        if potus not in potus_n_judges.keys():
            potus_n_judges[potus] = ["{} {}".format(line[0],line [1])]
        else:
            potus_n_judges[potus].append("{} {}".format(line[0],line [1]))

       
pres = raw_input("Enter President's name: ").lower()

matches = [names for names in potus_n_judges.keys() if names.find(pres) != -1]


if len(matches) == 0:
    print "Wasn't able to find the name!"
elif len(matches) == 1:
    for match in potus_n_judges[matches[0]]:       
        print match
else:
    print "Found multiple matches! ({} presidents!)".format(len(matches))
    for match in matches:
        for judge in potus_n_judges[match]:
            print "{} by {}".format(judge,match.title())