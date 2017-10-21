import mytime, datetime
class task:
    def __init__(self, taskstr):
        self.taskstr = taskstr
        self.find_event()
        
    def find_event(self):
        time_word = [' on ']
        for word in time_word:
            if word in self.taskstr:
                self.time = self.taskstr[len(word)+self.taskstr.index(word):]
                self.better_time()
                self.event = self.taskstr[:self.taskstr.index(word)]
                return
        self.daysleft = 100
        self.event = self.taskstr
    def better_time(self):
        today = datetime.date.today()
        day1 = datetime.timedelta(days = 1)
        if self.time in mytime.daylist:
            i = 0
            goalday = None
            while (today+i*day1).weekday() != mytime.daylist.index(self.time):
                i += 1
                if i > 30:
                    print('something wrong with the time left function')
                    break
            self.date = today+i*day1
            self.daysleft = i
        else:
            #print(self.time)
            month, day = self.time.split('.')
            self.date = datetime.date(today.year, int(month), int(day))
            if self.date<today:
                self.date = datetime.date(today.year+1, month, day)
            self.daysleft = (self.date - today).days
    def __repr__(self):
        return self.event
            
class many_tasks():
    def __init__(self, all_mytasks):
        self.task_list = []
        for i in all_mytasks:
            self.task_list.append(task(i))
        self.sort_all()
    
        
    def sort_all(self):
        import operator
        self.task_list = sorted(self.task_list, key=operator.attrgetter('daysleft'))
        
            
if __name__=="__main__":
    from tasks import things
    a = many_tasks(things)
    a = 'a'
            
