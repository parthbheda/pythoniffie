#we are using the datetime
#the module fetches local date and time
from datetime import datetime
#the datetime.now() method grabs the latest datetime
now = datetime.now()
#now.strftime converts the time to string format
current_time = now.strftime("%H:%M:%S")
print("Time is ", current_time)
#we convert the string format for hours into integers by typecasting
#we use if-else to create custom greetings
if(4 < int(now.strftime("%H")) < 12):
	print("Good morning")
else:
	print("Good evening")
