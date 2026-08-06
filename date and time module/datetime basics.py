from datetime import date
import time

# for module in dir(date):
#     print(module)

today_date = date.today()
ctime_now = today_date.ctime()
today_day = today_date.day

print("Date is : ", today_date)
print("Ctime is : ", ctime_now)
print("Day is : ", today_day)
print("Today dates toordinal : ", today_date.toordinal())
print("Todays weedday is : ", today_date.weekday())
print("Todays isoweekday is : ", today_date.isoweekday())
print("2023-01-01 isocalendar is : ", date(2023, 1, 1).isocalendar())
print("2023-01-02 isocalendar is : ", date(2023, 1, 2).isocalendar())
print("2023-01-03 isocalendar is : ", date(2023, 1, 3).isocalendar())
print("2023-05-18 isocalendar is : ", date(2023, 5, 18).isocalendar())
print("2023-12-31 isocalendar is : ", date(2023, 12, 31).isocalendar())
print("2025-01-01 isocalendar is : ", date(2025, 1, 1).isocalendar())

timestamp = time.time()
print("Timestamp is : ", timestamp)

datefromts = date.fromtimestamp(timestamp)
print("Date from TS is : ", datefromts)

datefromiso = date.fromisoformat('2000-01-01')
print(datefromiso)

print(datefromiso.replace(2019,5,18))
