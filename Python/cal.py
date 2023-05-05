import calendar
sdate=input().split()
mm,dd,yyyy=list(map(int,sdate))
print((calendar.day_name[calendar.weekday(yyyy,mm,dd)]).upper())