
import csv

#creating a dictionary of party values
party_values = {'I':'Independents','R':'Republicans','D':'Democrats'}


#Parsing the file
with open('Senate113.txt','r') as f:

    party_counts = dict()
    #Dictionary will contain party as and list of senators as value
    
    for row in csv.reader(f):
        party_code = row[2]
        #incrementing counts everytime a party is encountered
        party_counts[party_code] = party_counts.get(party_code,0) + 1


#prompting input for party value if not found
for party in party_counts:
    if party not in party_values.keys():
        party_values[party] = raw_input('Please enter party name for {}: '.\
        format(party))

#printing party values and counts
for each_party in party_counts:
    print '{}: {}'.format(party_values[each_party],party_counts[each_party])