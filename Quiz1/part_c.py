
import csv

def same_party(a_state):
    """Checks if a state has all senators from the same party"""
    parties = list()
    
    with open('Senate113.txt','r') as f:
        for row in csv.reader(f):
            state = row[1]
            party = row[2]
            
            #checking if state matches and party already in party list
            if party not in parties and state == a_state:
                parties.append(party)
        
    if len(parties) == 1:
        return True
    else:
        return False


with open('states.txt','r') as states_file:
    for line in states_file:
        state = line.strip()
        if same_party(state):
            print state