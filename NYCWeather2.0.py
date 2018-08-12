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
## Now to input into a sqlite3 DB
import sqlite3
c = sqlite3.connect('noaa.db')
try: ## if a table already existis, and you execute a create table an operational error will be thrown because it's trying to create another table that alrady exists(adding a new column after running could pose issue, essentially you have to delete db file and recreate it with new colum)
    c.execute('''CREATE TABLE mytable (
  id 		INTEGER PRIMARY KEY,
  Temperature 	DOUBLE,
  Today         Date,
  Recorded      INTEGER,
  WindSpeed     STRING,
  WindDirection STRING)''');
except sqlite3.OperationalError: #i.e. table exists already
    pass

#Prepared statement, protect against SQL Injection, note syntax
# think about question marks as place holders, positional arguments, date(now) wasnt being exexuted as sql so input after VALUES
c.execute('''INSERT INTO mytable(Temperature,Today,Recorded,WindSpeed,WindDirection) VALUES(?,Date('now'),?,?,?)''',
          (temp,time, wind, direction))
c.commit() # push to database
c.close()
