def protocol_aleks():
    import webbrowser
    input('Please hit enter when you have a pen, some papers, and a calculator.\nThe Aleks website will open by then.')
    webbrowser.open('https://www.aleks.com/')
    
def protocol_laundry():
    import itchat, wechatlib, threading, mytime, time
    laundrytimelist = []
    dryertimelist = []
    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        if msg['User']['PYInitial'] == "FYX":
            if msg.text == 'a':
                laundrytimelist.append(mytime.dateanalyze())
                return 'Laundry time recorded!'
            elif msg.text == 'b':
                dryertimelist.append(mytime.dateanalyze())
                return 'Dryer time recorded!'
                
        else:
            pass    
    
    itchat.auto_login(hotReload=True)
    wechatlib.sendmes(itchat, "Laundry protocol initiated! Please respond 'a' when the washing is running or 'b' when the dryer is running.")
    reply = threading.Thread(target=itchat.run)
    reply.start()
    while True:
        i = 0
        while i <= len(laundrytimelist)-1:
            n = mytime.dateanalyze()
            now = n.hour*60+n.minute
            itime = laundrytimelist[i].hour*60+laundrytimelist[i].minute
            if now>=itime+32:###########################
                wechatlib.sendmes(itchat, "The washing is ready in 5 minutes")
                del laundrytimelist[i]
            i += 1
        i = 0
        while i <= len(dryertimelist)-1:
            n = mytime.dateanalyze()
            now = n.hour*60+n.minute
            itime = dryertimelist[i].hour*60+dryertimelist[i].minute
            if now>=itime+30:############################
                wechatlib.sendmes(itchat, "The dryer is ready in 5 minutes")
                del dryertimelist[i]
            i += 1  
        time.sleep(10)
        
def protocol_relax():
    import pygame, time, threading, playvideo
    from mutagen.mp3 import MP3
    i = "In My Life-SFZVpSIaavA..mp3"
    audio = MP3(i)
    mix = pygame.mixer
    mix.init(frequency=audio.info.sample_rate)        
    mix.music.load(i)
    mix.music.play(0)
    time.sleep(audio.info.length)
    mix.quit()     
    
def protocol_programming():
    print('Program now!')
    
    
if __name__=="__main__":
    protocol_relax()
