# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    assert x, y
    if x >= 0 and y >= 0:

        if  isinstance(x,int) == True and isinstance(y,int) == True:

            result = sum(x, y)
            if result <= 200:
                assert isinstance(result, int)
                return result
            else:
                pass
        else:
            pass
    else:
        pass








