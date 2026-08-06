import calendar


c = calendar.Calendar(6)

for item in c.iterweekdays():
    print(item, end=' ')
print()

for item in c.itermonthdates(2023, 5):
    print(item, end=" ")
print()

for item in c.itermonthdays(2023, 5):
    print(item, end=" ")
print()

print("Below prints date in that month and day of the week")
for item in c.itermonthdays2(2023, 5):
    print(item, end=" ")
print()

print("Below prints tuple of (yyyy, mm, dd) in that calendar month")
for item in c.itermonthdays3(2023, 5):
    print(item, end=" ")
print()

print("Below prints tuple of (yyyy, mm, dd, dayof the week) in that calendar month")
for item in c.itermonthdays4(2023, 5):
    print(item, end=" ")
print()

print("Below prints a list of tuples in week format (dayofmonth weekday)")
for data in c.monthdays2calendar(2023, 5):
    print(data)
