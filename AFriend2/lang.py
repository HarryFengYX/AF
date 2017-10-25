#language tool kit
def find_verb(sent): #find verb of the sentence
    return sent.split(' ')[0]

def find_vars(cmd, struct):
    same_list = []
    keywords = [i for i in struct.split(' ') if i[0] != '@']
    for i in cmd.split(' '):
        if i in keywords: #if is keyword, then append
            same_list.append(i)
        else: #if not keyword, make a list
            if type(same_list[-1]) == list:
                same_list[-1].append(i)
            else:
                same_list.append([i])
    var2name = {}
    num = 0
    for i in struct.split(' '):
        if i[0] == '@': #if var detected, put the var and thing into the dict
            var2name[i[1:]]=' '.join(same_list[num]) #dict thing
        num += 1
    return var2name

def find_property(name):
    def lastindex(thel, thestr):
        return len(thel) - 1 - thel[::-1].index(thestr) #inverty the string and substring and use index
    if 'of' not in name:
        return False
    else: #let's don't think about multiple properties right now.
        listyname = name.split(' ') #make it a list for convenience
        last_of = lastindex(listyname,'of') #find the index of last of
        the_p = listyname[:last_of] #find the things before of
        #imme_p = the_p[lastindex(the_p,'of')+1:] #find the immediate property
        #rest_p = the_p[:lastindex(the_p,'of')] #find the rest property
        obj_name = listyname[last_of+1:] #find the obj's name
        #print('obj_name',obj_name)
        import fakememory
        for i in fakememory.objectlist:
            #print(i.name)
            if i.name == ' '.join(obj_name):
                the_obj = i
                break
        import properties
        new_obj = getattr(properties,' '.join(the_p))(the_obj) #find new obj, imme property of the obj
        return new_obj
