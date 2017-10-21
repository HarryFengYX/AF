from threading import *
from tkinter import *

def dt(timeobj):  
        return str(timeobj.hour)+':'+str(timeobj.minute)

def gtk():
        root = Tk()
        root.geometry("500x500")
        return root

def ctt(alarm,v):
    
        v.set("Timing right now!")
        tobj = Thread(target=timing, args=[alarm, v])
        tobj.start()

def timing(alarm, v):
        while True:
                now = dt(datetime.datetime.now())
                if alarm == now:
                        v.set("alarm!")
                time.sleep(10)

def musictl(event):
        print(crelaxt(e.get()))
        


if __name__=="__main__":
        import datetime
        import time
        from tkinter import *
        from timec import *


        alarm = "13:37"
        root1 = gtk()
        Label(root1,text="When do you work?").pack()
        e = Entry(root1, text="Hello")
        e.bind("<Key-Return>", musictl)
        e.pack()
        mainloop()




