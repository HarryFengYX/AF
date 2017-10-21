#main af file
import mytime, protocols, updateSchedule, time, datetime, threading

#get today's week, date, time. Find the schedule for today.
now = datetime.datetime.now()
today = datetime.date.today()
#schedule = myschedule.schedule[mytime.daylist[today.weekday()]]
def next_weekday(weekday):
    import datetime, mytime
    today = datetime.date.today()
    day1 = datetime.timedelta(days = 1)
    if weekday in mytime.daylist:
        i = 0
        goalday = None
        while (today+i*day1).weekday() != mytime.daylist.index(weekday):
            i += 1
            if i > 30:
                raise NameError('something wrong with the time left function')
                break
        date = today+i*day1
        return date
    else:
        raise NameError('Not valid weekday')
#do if near the event.
def checkevents(schedule):
    #checking what to do
    state = False
    for event in schedule:
        event_time = datetime.datetime(today.year, today.month, today.day, int(event.start.split(':')[0]), int(event.start.split(':')[1]))
        #print(event_time >= now)
        if (now >= event_time) and (datetime.date(today.year, event.exeday.month, event.exeday.date) < today):
            state = True
            print('Not executed today!')
            #find the protocl
            myp = getattr(protocols, 'protocol_thing'.replace('thing', event.name))
            myp()
            print('Done!')
            #change exeday to now.date
            updateSchedule.update()
        
    return state

print('Checking...')
while True:
    import myschedule
    schedule = myschedule.schedule[mytime.daylist[today.weekday()]]
    
    state = checkevents(schedule)
    if not state:
        print('nothing to do right now.')
        time.sleep(120)
    
