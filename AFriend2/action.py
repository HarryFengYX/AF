#action module
def put(arguments):
    obj, position = arguments #for univerality, I make the input a list
    obj.position = position #change the position of the object
    return obj #return the object

info = [
    {
    'name':'put', #name of the function, for finding the function by name
    'arguments':{'obj':'rect', 'position':'position'}, #arguments of the function, so the program know what kind of
    'struct':'put @obj on @position',
    }
]
