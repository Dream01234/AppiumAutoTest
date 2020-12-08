import datetime
import time
star = datetime.datetime.now()
i = 0
while i <10:
    y = i + 1
    print(y)
    i = i + 1
    time.sleep(1)
end = datetime.datetime.now()
time = end - star
print(time)
if  time.total_seconds() > 10:
    print("大于10")
else:
    print("小于10")