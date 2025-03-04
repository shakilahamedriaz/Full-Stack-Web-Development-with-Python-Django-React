# Import necessary modules
import pytz, datetime  
from datetime import datetime, UTC  
import time

# UTC - Coordinated Universal Time  
# 'UTC' is a built-in constant in Python 3.11+ for UTC time

# Define the timezone for Dhaka, Bangladesh  
dhaka = pytz.timezone('Asia/Dhaka')  

# Get the current UTC time  
utc = datetime.now(UTC)  

# Convert UTC time to Dhaka timezone and print  
# print(utc.astimezone(dhaka))  

# Print the current UTC time  
print(utc)  


# 2025-03-05 02:47:46.381746+06:00
# 2025-03-04 20:47:46.381746+00:00

# list of all timezone in the world
print(pytz.all_timezones)


#pause the program execution for 5 seconds before continuing.
start = datetime.now()
time.sleep(5)  # 5 sec er jonne code execution thamiye dibe
end = datetime.now()

print(end - start)