from datetime import datetime, timedelta

today = datetime.today().date()

#adding subtracting date
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(f"Today : {today}\nTomorrow: {tomorrow}\nYesterday: {yesterday}")
# output:
# Today : 2025-03-05
# Tomorrow: 2025-03-06
# Yesterday: 2025-03-04


#adding subtracting time
now = datetime.today()
new_time = now + timedelta(hours=10, minutes=1, seconds= 1, microseconds= 1)

print(now)
print(new_time)
#output:
# 2025-03-05 02:23:34.888624
# 2025-03-05 12:24:35.888625

date1 = datetime(2025, 12, 25)
date2 = datetime(2025, 12, 5)

print(date1 - date2)
#output:
#20 days, 0:00:00



