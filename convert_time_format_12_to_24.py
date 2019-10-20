#A simple if-else program 
#Python program to convert time 
# from 12 hour to 24 hour format 

# Function to convert the date format 
def convert_12_to_24(time_str): 
	
	 
	if time_str[-2:] == "AM" and time_str[:2] == "12": 
		return "00" +  time_str[2:-2] 
		
	elif time_str[-2:] == "AM": 
		return time_str[:-2] 
	
	elif time_str[-2:] == "PM" and time_str[:2] == "12": 
		return time_str[:-2] 
		
	else: 
		
		return str(int(time_str[:2]) + 12) + time_str[2:8] 

# example		 
print(convert_12_to_24("12:05:45 PM")) 
