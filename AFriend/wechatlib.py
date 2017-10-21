# -*- coding: utf-8 -*-
def sendmes(itchat,mes):
    #import itchat
    NickName = u"馮寅軒"
    a = itchat.search_friends(nickName = NickName)[0]
    itchat.send(mes, toUserName=a['UserName']) 