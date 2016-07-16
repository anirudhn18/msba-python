
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

word = raw_input('Enter a word:')

letters = np.unique(list(word))
letter_counts = [word.count(letter) for letter in letters]

counts_series = Series(letter_counts, index = letters)

for letter in counts_series.index.values:
    print '{} {}'.format(letter,counts_series.ix[letter])