

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    itemList = [x for x in skus]
    for item in itemList:
        if item not in ['A','B','C','D','E']:
            return -1

    As = [x for x in itemList if x == 'A']
    Bs = [x for x in itemList if x == 'B']
    Cs = [x for x in itemList if x == 'C']
    Ds = [x for x in itemList if x == 'D']
    Es = [x for x in itemList if x == 'E']

    LenA = len(As)
    offer200_RemainderA = LenA % 5
    offer200_QuotientA = LenA // 5

    SingularA = offer200_RemainderA % 3
    offer150_QuotientA = offer200_RemainderA // 3



    LenC = len(Cs)

    LenD = len(Ds)

    LenE = len(Es)
    RemainderE = LenE % 2
    QuotientE = LenE // 2


    LenB = len(Bs)
    LenB -= QuotientE
    RemainderB = LenB % 2
    QuotientB = LenB // 2

    print(LenA, LenB, LenC, LenD, LenE)
    finalPrice = (SingularA * 50) + (offer150_QuotientA * 130) + (offer200_QuotientA * 200) + (RemainderB * 30) + (QuotientB * 45) + (LenC * 20) + (LenD * 15)  + (LenE * 40)
    return finalPrice




