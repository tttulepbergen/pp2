#Write a Python program to subtract five days from current date.

from datetime import timedelta, datetime

currdate = datetime.now()
minfive = currdate - timedelta(days=5)

print("today", currdate.strftime("%Y-%m-%d"))
print("5 days ago", minfive.strftime("%Y-%m-%d"))




#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

current = datetime.now()
yesterday = current - timedelta(days=1)
tomorrow = current + timedelta(days=1)

print("yesterday", yesterday.strftime("%Y-%m-%d"))
print("current", current.strftime("%Y-%m-%d"))
print("tomorrow", tomorrow.strftime("%Y-%m-%d"))




#Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta

curr = datetime.now()
curr = curr.replace(microsecond=0)  

print(curr)




#Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

curr = datetime.now()
tmrw = curr + timedelta(days=1)

diff = (curr - tmrw).total_seconds()  # Вычисляем разницу в секундах
print(diff)




