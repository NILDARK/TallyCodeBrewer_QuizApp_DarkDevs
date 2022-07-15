import rstr
import re
import datetime
a = rstr.xeger(r'[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d/[A-Z,0-9]{6}')
print(a)
x = datetime.datetime(year=2022, month=7, day=15,hour=23,minute=14)
print(x)
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(minutes = 120))
# b = "9a123456789"
# x = re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",b)
# # y = re.search("[0-9]",b)
# print(x)l̥