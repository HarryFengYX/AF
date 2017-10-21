import datetime

class time:
    def __init__(self, atime):
        self.hour, self.minute = atime.split(':')[:2]
        self.hour = int(self.hour)
        self.minute = int(self.minute)
        
class dateanalyze:
    def __init__(self):
        timelist = datetime.datetime.today().ctime().split(' ')
        if '' in timelist:
            timelist.remove('')
        self.weekday, self.month, self.date, self.time, self.year = timelist
        self.month2num()
        self.date2num()
        
        self.weekday = self.weekday.lower()
        self.hour, self.minute, self.sec = self.time.split(':')
        self.time2num()
    def month2num(self):
        if self.month in monthList:
            self.month = monthList.index(self.month)+1
    def date2num(self):
        self.date = int(self.date)
    def time2num(self):
        self.hour = int(self.hour)
        self.minute = int(self.minute)
        self.sec = int(self.sec)
        
class mydate:
    def __init__(self, monthdate):
        self.month, self.date = [int(i) for i in monthdate.split('/')]
        self.md = monthdate
        
    def __repr__(self):
        return self.md
        
    def __lt__(self, mydate2):
        if self.month < mydate2.month:
            return True
        elif self.month == mydate2.month:
            if self.date < mydate2.date:
                return True
            else:
                return False
        else:
            return False
        
    def __gt__(self, mydate2):
        if self.month > mydate2.month:
            return True
        elif self.month == mydate2.month:
            if self.date > mydate2.date:
                return True
            else:
                return False
        else:
            return False        
        
def less1greater(time1, time2):
    t1 = time(time1)
    t2 = time(time2)
    timedifference = 60*(t1.hour-t2.hour) + t1.minute-t2.minute
    if timedifference <= 1:
        return True
    
class event:
    def __init__(self, name, day, start, end, exeday):
        self.name = name
        self.day = day
        self.start = start
        self.end = end
        self.exeday = exeday
    def __repr__(self):
        return self.name
    
daylist = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
if __name__ == "__main__":
    pass