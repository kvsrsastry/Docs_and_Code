# Datetime
import datetime

# Working with datetime objects
print(datetime.datetime.now())
d1 = datetime.datetime(year=1980, month=5, day=23, hour=18, minute=15, second=34, microsecond=7777)
d2 = datetime.datetime(year=1981, month=2, day=4, hour=18, minute=18, second=25, microsecond=8888)
print(d1)
print(d2)
df = d1 - d2
print(df.days)
print(df.seconds)
print(d1.strftime(format='%Y-%m-%d %H:%M:%S.%f'))

# Working with date objects
print(datetime.date.today())
dt1 = datetime.date(year=1980, month=5, day=23)
dt2 = datetime.date(year=1981, month=2, day=4)
dtf = dt2 - dt1
print(dtf.days)
three_days_before = datetime.date.today() - datetime.timedelta(days=3)
#three_days_before = dt1 - datetime.timedelta(days=3)
print(three_days_before)
seven_days_after = datetime.date.today() + datetime.timedelta(days=7)
print(seven_days_after)

# Working with time objects
datetime.datetime.now().strftime(format='%H:%M:%S')
t1 = datetime.time(hour=23, minute=59, second=59)
t2 = datetime.time(hour=3, minute=9, second=8)
# Subtracting Time Objects
print(datetime.datetime.combine(datetime.date.min, t1) - datetime.datetime.combine(datetime.date.min, t2))
# 3 hours after t1
t1_plus_3 = datetime.datetime.combine(datetime.date.min, t1) + datetime.timedelta(hours=3)
print(t1_plus_3.strftime(format='%H:%M:%S'))
print(datetime.date.min)
print(datetime.date.max)
