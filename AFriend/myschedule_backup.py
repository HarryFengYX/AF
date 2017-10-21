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
        
        ],
    'fri':[
        
        ],
    'sat': [
        mytime.event('aleks', 'sat', '11:30', '12:00', mytime.mydate('10/14')),
        ],
    'sun':[
        
        ],
     
}
  
if __name__ == "__main__":
    print(schedule)
    