
item = raw_input("Please enter a description of the item: ")
cost = int(raw_input("Please enter the cost of the item: "))
est_life = int(raw_input("Please enter the estimated life of the item in whole years: "))
method = int(raw_input("Please enter depreciation method (1 = straight line, 2 = double declining balance): "))

print "Depreciation schedule for: {}\n".format(item)

print "   Year\t  Begin\t    Dep\t    End"

year = 0
begin = cost
dep = 0
end = cost
print  "{:7}    {:7.2f}    {:7.2f}    {:7.2f}".format(year,begin,dep,end)

while end > 0 :
    year += 1
    begin = end    

    if method == 1 :
        dep = float(cost)/est_life        
    elif method == 2 and year != est_life:
        dep = 2*float(begin)/est_life    
    else :
        dep = begin
            
    end = begin - dep
    print  "{:7d}    {:7.2f}    {:7.2f}    {:7.2f}".format(year,begin,dep,end)