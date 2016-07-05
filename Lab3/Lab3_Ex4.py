
def duplicate_names(name_list):
    name_counts = dict()
    
    for name in name_list:
        name_counts[name] = name_counts.get(name,0)  + 1
    
    dup_list = list()
    
    for name in name_counts:
        if name_counts[name] > 1:
            dup_list.append(name)
    return dup_list


list_of_names = ['Bob','Alice','Jerry','Jerry','Nathan','Alice']

print duplicate_names(list_of_names)