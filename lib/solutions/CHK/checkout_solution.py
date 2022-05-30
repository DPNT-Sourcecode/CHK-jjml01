
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
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'L': 90,
        'M': 15,
        'N': 50,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50
    }


    # Offers

    RemainderA200 = itemCount[0] % 5
    QuotientA200 = itemCount[0] // 5

    RemainderA150 = RemainderA200 % 3
    QuotientA150 = RemainderA200 // 3

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
    finalPrice = (RemainderA150 * 50) + (QuotientA150 * 130) + (QuotientA150 * 200) + (RemainderB * 30) + \
                (QuotientB * 45) + (itemCount[2] * 20) + (itemCount[3] * 15) + (itemCount[4] * 40) + (itemCount[5] * 10)
    return finalPrice



