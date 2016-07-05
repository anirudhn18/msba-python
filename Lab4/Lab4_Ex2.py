

with open('States.txt','r') as f:
    for line in f:
        if 'New' in line.split():
            print line
