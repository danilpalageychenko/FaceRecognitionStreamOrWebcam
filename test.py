#import datetime
#from datetime import timedelta, datetime
from datetime import datetime

str = "ОБАНАРУЖЕННО:....Дата: 11-01-2020 15:14 Призвище особи - Danil"
qwe = str.split(" ")
print(qwe[1] + " " + qwe[2], qwe[-1])




now = datetime.now()
data = datetime.strptime(qwe[1] + " " + qwe[2],'%d-%m-%Y %H:%M')
print(data)
print(now)
#print((now-0).seconds)