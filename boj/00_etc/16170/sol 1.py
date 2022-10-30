from time import localtime, time

tm = localtime(time())
print(tm.tm_year)
print(tm.tm_mon)
print(tm.tm_mday)