from datetime import datetime, timedelta
d1, m1 = map(int, input().split())
d2, m2 = map(int, input().split())
data1 = datetime(year=2023, month=m1, day=d1)
data2 = datetime(year=2023, month=m2, day=d2)
dif = (data2-data1).days
print(dif)
