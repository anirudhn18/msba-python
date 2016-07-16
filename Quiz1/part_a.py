#Program to prompt user for state and return its senators
import csv

#Parsing the file
with open('Senate113.txt','r') as f:

    senator_dict = dict()    
    #Dictionary will contain state as the key and list of senators as value
    
    for row in csv.reader(f):

        #Using lower to enable partial matching
        state = row[1].lower()
        senator = row[0]
        
        if state not in senator_dict.keys():
            senator_dict[state] = [senator]
        else:
            senator_dict[state].append(senator)


#prompting user input
input_state = raw_input('Enter your state: ').lower()

#getting a list of all state matches
matches = list()

for each_state in senator_dict:
    if each_state.find(input_state) != -1:
        matches.append(each_state)

if len(matches)==0:
    print 'No matches found!'

elif len(matches) == 1:
    print 'Your US senators are: '
    for senator in senator_dict[matches[0]]:
        print '{}'.format(senator)

else:
    print 'Multiple matches ({}) were found!'.format(len(matches))
    print 'Your US senators are: '

    #printing all senator names for each state match
    for match in matches:
        print 'from {}:'.format(match.title())
        for senator in senator_dict[match]:
            print '\t{}'.format(senator)