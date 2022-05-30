
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # Initialisation, input handling

    skuList = list(map (chr, range(65,91)))
    itemList = [x for x in skus]
    for item in itemList:
        if item not in skuList:
            return -1

    # Item handling

    itemBreakdown = [[0] for x in skuList]
    print('itemBreakdown final',itemBreakdown)
    for item in skuList:

        itemBreakdown[skuList.index(item)] += [1 for x in itemList if x == skuList[skuList.index(item)]]
        if len(itemBreakdown[skuList.index(item)]) > 1:
            itemBreakdown[skuList.index(item)].pop(0)
    print('itemBreakdown final',itemBreakdown)
    itemCount = [sum(x) for x in itemBreakdown]

    # Price dictionary

    priceDict = {

        
    }


    # Offers

    offer200_RemainderA = itemCount[0] % 5
    offer200_QuotientA = itemCount[0] // 5

    offer150_RemainderA = offer200_RemainderA % 3
    offer150_QuotientA = offer200_RemainderA // 3

    RemainderE = itemCount[4] % 2
    QuotientE = itemCount[4] // 2



    if itemCount[1] > 0:
        itemCount[1] -= QuotientE
    else:
        pass

    RemainderB = itemCount[1] % 2
    QuotientB = itemCount[1] // 2

    RemainderF = itemCount[5] % 3
    QuotientF = itemCount[5] // 3
    itemCount[5] -= QuotientF

    # Output

    print(itemCount)
    finalPrice = (offer150_RemainderA * 50) + (offer150_QuotientA * 130) + (offer200_QuotientA * 200) + (RemainderB * 30) + \
                (QuotientB * 45) + (itemCount[2] * 20) + (itemCount[3] * 15) + (itemCount[4] * 40) + (itemCount[5] * 10)
    return finalPrice


