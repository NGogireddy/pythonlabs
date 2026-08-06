import calendar


# print(calendar.calendar(2023, w=3, c=6, m=4, l=1))
calendar.setfirstweekday(calendar.SUNDAY)
# calendar.prcal(2023, w=2, c=6, m=6, l=1)
#
# print(calendar.month(1984, 6, 3))
# calendar.setfirstweekday(calendar.TUESDAY)
# calendar.prmonth(1986, 7, 3, 2)

print(calendar.weekday(2023, 7, 18))

header = calendar.weekheader(10)
print(type(header))
print(header)

print(calendar.isleap(1600))
print(calendar.leapdays(2000,2021))
