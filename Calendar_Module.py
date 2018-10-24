import calendar

n = input()
calendarList = n.split(" ")

print (calendar.day_name[calendar.weekday(int(calendarList[2]),int(calendarList[0]),int(calendarList[1]))].upper())


# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
