import calendar


class MyCalendar():
    def count_weekday_in_year(self, yr=2020, day=0):
        counter = 0
        c = calendar.Calendar()
        for i in range(1,13):
            for data in c.monthdays2calendar(yr, i):
                # print(data)
                for x, y in data:
                    if x>0 and y==day:
                        counter += 1
        return(counter)


mycal = MyCalendar()
print(mycal.count_weekday_in_year(2000,0))
print(mycal.count_weekday_in_year(2000,1))
print(mycal.count_weekday_in_year(2000,2))
print(mycal.count_weekday_in_year(2000,3))
print(mycal.count_weekday_in_year(2000,4))
print(mycal.count_weekday_in_year(2000,5))
print(mycal.count_weekday_in_year(2000,6))
