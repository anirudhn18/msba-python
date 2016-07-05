import json
     
with open('USStates.json','r') as jsonfile:
    usstates = json.load(jsonfile,'utf-8')

pop_densities = dict() 

#Looping through the dictionary and calculating pop density
for state in usstates.keys():    
    pop_density = float(usstates[state]['pop'])/float(usstates[state]['area'])    
    pop_densities[pop_density] = usstates[state]['name']
    
for dens in sorted(pop_densities, reverse = True):
    print "{:15s}    {:<7.2f}".format(pop_densities[dens],dens)