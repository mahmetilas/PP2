# Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

today = datetime.now()
five_d_a = today - timedelta(days=5)

print(five_d_a.strftime('%Y-%B-%d'))
# ---------------------------------------------------------------------------------------------------------------
# Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(yesterday.strftime('%Y-%B-%d'))
print(today.strftime('%Y-%B-%d'))
print(tomorrow.strftime('%Y-%B-%d'))
# ---------------------------------------------------------------------------------------------------------------
# Write a Python program to drop microseconds from datetime.
from datetime import datetime, timedelta

today = datetime.now()
print(today.strftime('%Y-%m-%d %H:%M:%S'))
# ---------------------------------------------------------------------------------------------------------------
# Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference = date2 - date1

seconds = abs(difference.total_seconds())

print("Difference in seconds:", int(seconds))