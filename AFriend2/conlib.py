#this is the library for consciousness


def verb(sent): #using the lang module to find verb
    import lang
    return lang.find_verb(sent)

def info_by_verb(verb): #using the action module to find info of the verb
    import action
    for i in action.info:
        if i['name'] == verb:
            return i
    return False

def cant_understand():
    print("Sorry, I don't understand") #do something so the master know what is wrong
    return

def vars(cmd, struct): #find the strs that correspond to the vars
    import lang
    return lang.find_vars(cmd, struct)

def find_obj(name, the_type): #find 1 object regarding to the the name
    import fakememory
    for obj in fakememory.objectlist:
        if (obj.type == the_type) and (obj.name == name):
            return obj
    return False

def objects(var2name, info): #find all objects, if unsuccessful, try analyze
    name2obj = {}
    for i in var2name.keys():
        name = var2name[i]
        a = find_obj(name, info['arguments'][i]) #name and type of the object, returning the obj
        if a:
            name2obj[name] = a
        else:
            import lang
            new_obj = lang.find_property(name) #get the obj thing for later
            name2obj[name] = new_obj
    return name2obj

def act(info, objs):
    import action
    myaction = getattr(action, info['name'])
    return myaction(objs)
