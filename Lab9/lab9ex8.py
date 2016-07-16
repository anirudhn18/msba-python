
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

fortune500 = pd.read_csv('Files/fortune500.csv',na_values = 'N.A.',thousands=',')

fortune500.rename(columns = {'Revenue (in millions)':'Revenue',
                             'Profit (in millions)':'Profit'},inplace = True)


print '#1'
print 'How many (if any) companies have been in top 50 all 55 years?\n'

company_counts_top50 = fortune500['Company'][fortune500['Rank']<=50].value_counts()

for company in company_counts_top50.index:
    if company_counts_top50[company]==55:
        print company
        

print '\n\n\n#2'
print 'Which companies\' standing has had the most drops/rises(top ten)?'
print '(Considering companies that appear at least 25 times)\n'

company_counts = fortune500['Company'].value_counts()

rank_diff  = DataFrame(\
                    {'Company':company_counts[company_counts>=25].index},
                    index = company_counts[company_counts>=25].index)

#Some years have ranking till 1000 as well
fortune500_filtered = fortune500[ (fortune500['Company'].\
                        isin(rank_diff['Company'])) & \
                        (fortune500['Rank']<=500) ]

#Getting min and max for each company
rank_diff['max_rank'] = fortune500_filtered.groupby('Company').max()['Rank']
rank_diff['min_rank'] = fortune500_filtered.groupby('Company').min()['Rank']

rank_diff['rank_difference'] = rank_diff['max_rank'] - rank_diff['min_rank']

top_differences = rank_diff[rank_diff['rank_difference'].\
                        rank(method = 'first', ascending = False) <= 10]

for company in top_differences['Company']:
    print '{} had a variation of {} ranks'.format(company,\
                    top_differences['max_rank'].ix[company])
                    
                    
                    
print '\n\n\n#3'
print 'On an average, how much wealth is focused in the top 10?'


wealth_gap = DataFrame({'year':fortune500['Year'].unique(),
             'top5':fortune500[fortune500['Rank']<=5].groupby('Year').sum()['Revenue'],
             'rest':fortune500[(fortune500['Rank']>=5) &\
             (fortune500['Rank']<=500)].groupby('Year').sum()['Revenue']})

wealth_gap['pct'] = wealth_gap['top5']/(wealth_gap['rest'] + wealth_gap['top5'])

print '{:.2f}% !'.format(wealth_gap['pct'].mean()*100)