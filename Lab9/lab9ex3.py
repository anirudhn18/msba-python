
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

names = list(pd.read_csv('Files/names2.txt',squeeze = True,header = None))
unique_names = np.unique(names)

counts = DataFrame({'names':unique_names,\
                    'counts':[names.count(name) for name in unique_names]})

list(counts[counts['counts'] > 1]['names'])