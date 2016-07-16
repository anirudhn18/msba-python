
from pandas import Series, DataFrame
import pandas as pd

teams = Series(['Jazz','Jets','Owls','Rams','Cubs','Zips'])

results = DataFrame({'Jazz':[None,True,True,False,False,True],
         'Jets':[False ,None ,True ,True ,False ,False],
         'Owls':[False ,False ,None ,False ,True ,True],
         'Rams':[True ,False ,True ,None ,True ,True],
         'Cubs':[True ,True ,False ,False ,None ,True],
         'Zips':[False ,True ,False ,False ,False ,None]},index=teams)

print results.sum().sort_values(ascending = False).astype(int)