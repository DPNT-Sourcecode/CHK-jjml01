

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    itemList = [x for x in skus]
    for item in itemList:
        if item not in ['A','B','C','D']:
            return -1

    As = [x for x in itemList if x == 'A']
    Bs = [x for x in itemList if x == 'B']
    Cs = [x for x in itemList if x == 'C']
    Ds = [x for x in itemList if x == 'D']

    LenA = len(As)
    RemainderA = LenA % 3
    QuotientA = LenA // 3
    LenB = len(Bs)
    RemainderB = LenB % 2
    QuotientB = LenB // 2
    LenC = len(Cs)
    LenD = len(Ds)
    print(LenA, LenB, LenC, LenD)
    finalPrice = (RemainderA * 50) + (QuotientA * 130) + (RemainderB * 30) + (QuotientB * 45) + (LenC * 20) + (LenD * 15)
    return finalPrice





