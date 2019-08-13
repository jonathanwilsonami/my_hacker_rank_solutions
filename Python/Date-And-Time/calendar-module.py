#Calendar Module
import calendar

date = input()

date = date.split(" ")
result = calendar.day_name[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))].upper()
print(result)
