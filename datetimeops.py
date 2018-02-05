import time
import datetime

print ("Time in seconds since the epoch: %s" %time.time())
print (time.localtime(time.time()))
localtime = time.asctime(time.localtime(time.time()) )
print ("Local current time :", localtime)

print ("Current date and time: " , datetime.datetime.now())
print("Or like this YYYY-MM-DD Timestamp: ", datetime.datetime.today())
print("Or like this YYYY-MM-DD: ", datetime.date.today())
print ("Or like this YY-MM-DD-HH-MM: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
print ("Current year YYYY : ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%m"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w"))
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))
