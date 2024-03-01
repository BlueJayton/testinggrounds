import datetime

# get current date
today = datetime.date.today()

# get current week's starting day (Monday)
week_start = today - datetime.timedelta(days=today.weekday())

# get current week's ending day (Sunday)
week_end = week_start + datetime.timedelta(days=5)

# print results
print("Today's date:", today)
print("Current week's starting day:", week_start)
print("Current week's ending day:", week_end)
