#this is a file, often rewritten by program, records all the weekly events in time order

import mytime 

schedule = {
    'mon':[
        ],
    'tue':[
        ],
    'wed':[
        ],
    'thu':[
        mytime.event('chemistry_report', 'thu', '18:00', '20:00', mytime.mydate('10/21')),
        ],
    'fri':[
        ],
    'sat':[
        mytime.event('programming', 'sat', '16:15', '12:00', mytime.mydate('10/21')),
        mytime.event('aleks', 'sat', '11:00', '12:00', mytime.mydate('10/21')),
        ],
    'sun':[
        mytime.event('laundry', 'sun', '13:30', '99:99', mytime.mydate('10/21')),
        ],

}


if __name__ == "__main__":
    print(schedule)