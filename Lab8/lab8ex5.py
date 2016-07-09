
import numpy as np



#1
#HAS THE UNIQUE NUMBER OF NAMES INCREASED OVER TIME?

#for this, we will take the total names in each files and obtain
#the correlation between the year and the number of names for that year

#Note: If a name is both male and female, it is counted as different names

years = range(1880,2016)
name_counts = list()

for year in years:
    name_data = np.loadtxt('Files/names/yob{}.txt'.format(year),\
                    delimiter = ',', usecols = [0], dtype = str)
    
    name_counts.append(len(name_data))
    
print np.corrcoef(years,name_counts)
#
#[[ 1.          0.93806389]
# [ 0.93806389  1.        ]]

#From the correlation matrix we can see that the number of names and the year of
#birth is highly positively correlated. THus, THE UNQIUE NUMBER OF NAMES 
#INCREASES WITH TIME




#2
#ARE THERE MORE MALE NAMES OR FEMALE NAMES?

#for this we will take the yearly split of male and female name and 
#compare the number of years that each sex has higher uniqueness

higher_gender = list()

for year in years:
    name_data = np.loadtxt('Files/names/yob{}.txt'.format(year),\
                    delimiter = ',', usecols = [1], dtype = str)
    
    male_count = len([row for row in name_data if row == 'M'])
    female_count = len([row for row in name_data if row == 'F'])
    
    if male_count > female_count:
        higher_gender.append('M')
    elif female_count > male_count  :
        higher_gender.append('F')
    else :
        higher_gender.append('Eq')

counts = { gender:higher_gender.count(gender) for gender in higher_gender}

print counts
#{'M': 3, 'F': 133}

#From the counts, it is apparent that there are more female names than there 
#are male ones for almost 98% of the years




#3
#HAS THE NUMBER OF UNISEX NAMES INCREASED OVER THE YEARS?

#For this we will take all names which appear in both lists and see if the % of 
#such names has any correlation with the year (similar to first question)

common_counts = list()

for year in years:
    name_data = np.loadtxt('Files/names/yob{}.txt'.format(year),\
                    delimiter = ',', usecols = [0,1], dtype = str)
    
    male_names = [row[0] for row in name_data if row[1] == 'M' ]
    female_names = [row[0] for row in name_data if row[1] == 'F']
    
    common_counts.append(sum(np.in1d(male_names,female_names))/float(len(name_data)))


print np.corrcoef(years,common_counts)
#[[ 1.         -0.09387398]
# [-0.09387398  1.        ]]


#We can see that the % of Unisex names display no strong correlation with the 
#years