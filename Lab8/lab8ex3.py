
import numpy as np


teams = np.array(['Jazz','Jets','Owls','Rams','Cubs','Zips'])

results = np.array([[None,True,True,False,False,True],
         [False ,None ,True ,True ,False ,False],
         [False ,False ,None ,False ,True ,True],
         [True ,False ,True ,None ,True ,True],
         [True ,True ,False ,False ,None ,True],
         [False ,True ,False ,False ,False ,None]])


team_wins = list()

for i in range(0,len(teams)):
    team_wins.append((teams[i] , sum([result for result in results[i] \
                                      if result != None ])))

team_wins=np.array(team_wins)

#getting ascending order of indices
asc_order = np.transpose(np.argsort(team_wins,axis=0))[1]


for i in range(0,len(asc_order)):
    position = asc_order[len(asc_order) - i -1]
    
    print "{} {}".format(team_wins[position][0],team_wins[position][1])