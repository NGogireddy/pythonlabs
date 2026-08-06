from datetime import time
from datetime import timezone
from datetime import timedelta, datetime

timenow = time(14, 5, 30, 124)
print(timenow)

tz = timezone(timedelta())
print(tz.tzname(datetime(2000, 4, 5)))
print(tz.dst(datetime(2000, 4, 5)))
