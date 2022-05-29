# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):

    if  isinstance(x,int) and isinstance(y,int):
        
        result = sum(x, y)

    assert isinstance(result, int)
    return result   


