from datetime import datetime
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

dt = datetime(2020, 11, 4, 14, 53)
print(dt)
print(dt.strftime('%y/%B/%d %H:%M:%S %p'))
print(dt.strftime('%a, %Y %b %d'))
print(dt.strftime('%A, %Y %B %d'))
print('Weekday : ', dt.strftime('%w'))
print('Day of the year : ', dt.strftime('%j'))
print('Week number of the year : ', dt.strftime('%U'))
