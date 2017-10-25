#this is the consciousness of the whole program
import conlib
cmd = 'put rect1 on center of the screen' #let us set the command this way
verb = conlib.verb(cmd) #find the verb in this command so we can continue
info = conlib.info_by_verb(verb) #get the dictionary info or an error
if not info:
    conlib.cant_understand()
    quit()
var2name = conlib.vars(cmd, info['struct'])
