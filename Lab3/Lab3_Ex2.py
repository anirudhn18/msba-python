
word = raw_input('Enter a word: ')

histogram = dict()

# count each letter
for char in word:
    histogram[char] = histogram.get(char,0) + 1
        
# print the results
#using sorted() function to sort the dictionary
for char in sorted(histogram):
    print '{0} {1}'.format(char,histogram[char])