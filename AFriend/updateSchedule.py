#updateSchedule
import myschedule, mytime
schedule = myschedule.schedule
now = mytime.dateanalyze()
def update():
    filecomment = '#this is a file, often rewritten by program, records all the weekly events in time order'
    fileimport = 'import mytime '
    fileschedule = 'schedule = {\n'
    for day in mytime.daylist:
        fileschedule += "    'day':".replace('day', day) + '[\n'
        for event in schedule[day]:
            fileschedule += '        mytime.event(' 
            fileschedule += ', '.join(["'"+event.name+"'", "'"+event.day+"'", "'"+event.start+"'", "'"+event.end+"'", "mytime.mydate('date1'))".replace('date1', str(now.month)+'/'+str(now.date))])
            fileschedule += ',\n'
            
        fileschedule += '        ],\n'
    fileschedule += '\n}\n'
    filetest = 'if __name__ == "__main__":\n    print(schedule)'
    filestr = '\n\n'.join([filecomment,fileimport,fileschedule,filetest])
    with open('myschedule.py', 'w+') as m:
        m.write(filestr)
    
    if __name__== "__main__":
        print(filestr)

if __name__== "__main__":
    update()