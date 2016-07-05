import csv

class State:
    """Represents a US state"""
    def __init__(self,name,area,pop):
        self.name = name
        self.area = float(area)
        self.pop = float(pop)
    
    def pop_dens(self):
        self.popdens = self.pop/self.area
        

states = list()
        
with open('USStates.txt','r') as f:
    for row in csv.reader(f):
        state = State(row[0],row[2],row[3])
        state.pop_dens()
        
        states.append(state)
        
for each_state in states:
    print '{:s}: {:.2f}'.format(each_state.name,each_state.popdens)