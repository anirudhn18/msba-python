
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

baseball = pd.read_csv('Files/baseball.txt',header = None,\
                        names = ['Player','Team','At bat','Hits'])

baseball['Average'] = (baseball['Hits']/baseball['At bat']).round(3)

max_avg = baseball['Average'].max()

best_players = baseball['Player'][baseball['Average'] == max_avg]

for player in best_players:
    print player