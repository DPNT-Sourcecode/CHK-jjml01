

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skuList = ['A','B','C','D','E','F']
    itemList = [x for x in skus]
    for item in itemList:
        if item not in skuList:
            return -1

    itemBreakdown = [[0] for x in skuList]

    for item in skuList:
        
        itemBreakdown.append([x for x in itemList if x == skuList[skuList.index(item)]])

    itemCount = [len(x) for x in itemBreakdown]

    offer200_RemainderA = itemCount[0] % 5
    offer200_QuotientA = itemCount[0] // 5

    SingularA = offer200_RemainderA % 3
    offer150_QuotientA = offer200_RemainderA // 3



    LenC = len(Cs)

    LenD = len(Ds)


    RemainderE = itemCount[4] % 2
    QuotientE = itemCount[4] // 2


   LenB = itemCount[1]
    if LenB > 0:
        LenB -= QuotientE
    else:
        pass
    RemainderB = itemCount[1] % 2
    QuotientB = itemCount[1] // 2

    print(LenA, LenB, LenC, LenD, LenE)
    finalPrice = (SingularA * 50) + (offer150_QuotientA * 130) + (offer200_QuotientA * 200) + (RemainderB * 30) + (QuotientB * 45) + (LenC * 20) + (LenD * 15)  + (LenE * 40)
    return finalPrice
