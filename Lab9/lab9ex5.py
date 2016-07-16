
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

justices = pd.read_csv('Files/Justices.txt',usecols = [4,5],\
            names = ['yr1','yr2'])

#finding minimum year and maximum year
min_yr = min(justices[justices['yr2']>0].min())
max_yr = max(justices.max())

years = range(min_yr,max_yr+1)


#if number is not present in each column, the sum is 0
#Using this to return if the number is not present in the entire table
absent_years = [year for year in years \
                if sum(justices.isin([year]).sum()) == 0 ]

print absent_years