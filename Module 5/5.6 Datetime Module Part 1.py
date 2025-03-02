#Datetime module
import datetime

#date and time now
current_time = datetime.datetime.now()
print(current_time)
#2025-03-02 17:05:04.117743


#only date today
today_date = datetime.date.today()
print(today_date)
#2025-03-02


#today_time
today_time = datetime.datetime.now().time()
print(today_time)
#17:17:30.753480


#custom_datetime                    year month date 10 30 min
custome_datetime = datetime.datetime(2030, 2, 20, 10, 30, 0)
print(custome_datetime)
#2030-02-20 10:30:00

custome_datetime2 = datetime.datetime(2030, 2, 20, 10)
print(custome_datetime2)
#2030-02-20 10:00:00


formatted_date = current_time.strftime("%Y/%m/%d %H:%M:%S")  
print(formatted_date)
#2025/03/02 17:44:09

formatted_date2 = current_time.strftime("%y/%m/%d %H:%M:%S")
print(formatted_date2)
#25/03/02 17:45:37

formatted_date3 = current_time.strftime("%y/%B/%d %H:%M:%S")
print(formatted_date3)
#25/March/02 17:46:19


formatted_date4 = current_time.strftime("%y/%b/%d %H:%M:%S")
print(formatted_date4)
#25/Mar/02 17:46:19


formatted_date5 = current_time.strftime("%y/%b/%d %a %H:%M:%S")
print(formatted_date5)
#25/Mar/02 Sun 23:35:44

formatted_date6 = current_time.strftime("%y/%b/%a/%d %a %I:%M:%S")
print(formatted_date6)
#25/Mar/Sun/02 Sun 11:35:26

formatted_date6 = current_time.strftime("%y/%b/%a/%d %a %I:%M:%S %p")
print(formatted_date6)
#25/Mar/Sun/02 Sun 11:35:26 PM


print("ok")
date_str = "25-12-2030  10:45:00"
parsed_date = datetime.datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S") #convert date time object
print(parsed_date)
#2030-12-25 10:45:0 