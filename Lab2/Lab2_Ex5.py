
cloud_cover_pct = int(raw_input("Please enter the cloud cover (in %) between 0 to 100: "))

while not (cloud_cover_pct>=0 and cloud_cover_pct<=100):
    print "Enter a valid cloud cover percentage"
    cloud_cover_pct = int(raw_input("Please enter the cloud cover (in %) between 0 to 100: "))

if cloud_cover_pct <= 30:
    condition = "clear"
elif cloud_cover_pct >30 and cloud_cover_pct <= 70 :
    condition = "partly cloudy"
elif cloud_cover_pct >70 and cloud_cover_pct <= 99 :
    condition = "mostly cloudy" 
else:
    condition = "overcast"
    
print "It is {} today!".format(condition)