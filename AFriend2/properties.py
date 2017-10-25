#all properties
def center(obj):
    x = obj.width/2 +obj.position.x
    y = obj.height/2 +obj.position.y
    import concepts
    return concepts.position(x, y)
