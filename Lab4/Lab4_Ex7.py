import json

def kel_to_cnf(temp):
    cel = float(temp) - 273.15
    far = cel*1.8 + 32
    
    return [cel, far]
    

def parse_weather_data(day_data):
                
    cloud_cover = day_data['clouds']['all']
    temp = day_data['main']['temp']
    
    return cloud_cover,temp


with open('minneapolis.json','r') as jsonfile:
    raw_data = json.load(jsonfile)



temps=[]

#len(raw_data['list']) returns the number of days of data
for i in range(0,len(raw_data['list'])):    
        
    cloud,temp_day = parse_weather_data(raw_data['list'][i])
    
    if int(cloud) == 0 :
        temps.append(temp_day)

        
for temp in temps:
    print "{:.1f}C / {:.1f}F".format(kel_to_cnf(temp)[0],kel_to_cnf(temp)[1])