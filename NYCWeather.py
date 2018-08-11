from noaa_sdk import noaa # let's  pull daily local weather data
n = noaa.NOAA()
b = n.points_forecast(40.7314, -73.8656, hourly=False)
c = type(b)
d = b["properties"] # creating variable for dictionary

#for key in d.keys(): # let's take a look at the keys of this dictionary
    #print(key)
f = d["periods"] # periods is a list
g = f[3] # inside the periods list is a dictionary
# define variable to use 
wind = g["windSpeed"]#inside the dictionary, we call this key to get valuable data
temp = g["temperature"]
direction = g["windDirection"]
time = g["endTime"]

    
print('The weather in Queens, NY is ' + str(temp) + ' Degrees, with a wind speed of ' + wind + " coming from the  " + direction + " this data was reconciled from NOAA on the following date & during the following time range " + time + " enjoy the day!")
