# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Initialisation, input handling

    skuList = list(map(chr, range(65, 91)))

    itemList = [x for x in skus]
    for item in itemList:
        if item not in skuList:
            return -1

    # Item handling

    itemBreakdown = [[0] for x in skuList]
    print('itemBreakdown final', itemBreakdown)
    for item in skuList:

        itemBreakdown[skuList.index(item)] += [1 for x in itemList if x == skuList[skuList.index(item)]]
        if len(itemBreakdown[skuList.index(item)]) > 1:
            itemBreakdown[skuList.index(item)].pop(0)
    print('itemBreakdown final', itemBreakdown)
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
        'Z': 50,
        'A1': 200,
        'A2': 130,
        'B1': 45,
        'H1': 80,
        'H2': 45,
        'K1': 150,
        'P1': 200,
        'Q1': 80,
        'V1': 130,
        'V2': 90
    }
    priceDictList = priceDict.items()
    # Offers

    RemainderA200 = itemCount[0] % 5
    QuotientA200 = itemCount[0] // 5
    RemainderA150 = RemainderA200 % 3
    QuotientA150 = RemainderA200 // 3

    RemainderE = itemCount[4] % 2
    QuotientE = itemCount[4] // 2
    itemCount[1] -= QuotientE
    if itemCount[1] < 0:
        itemCount[1] = 0
    else:
        pass

    RemainderB = itemCount[1] % 2
    QuotientB = itemCount[1] // 2

    RemainderF = itemCount[5] % 3
    QuotientF = itemCount[5] // 3
    itemCount[5] -= QuotientF

    RemainderH80 = itemCount[7] % 10
    QuotientH80 = itemCount[7] // 10
    RemainderH45 = RemainderH80 % 5
    QuotientH45 = RemainderH80 // 5

    RemainderK = itemCount[10] % 2
    QuotientK = itemCount[10] // 2

    RemainderN = itemCount[13] % 3
    QuotientN = itemCount[13] // 3
    itemCount[12] -= QuotientN
    if itemCount[12] < 0:
        itemCount[12] = 0
    else:
        pass

    RemainderP = itemCount[16] % 5
    QuotientP = itemCount[16] // 5

    RemaindeR = itemCount[17] % 3
    QuotientR = itemCount[17] // 3
    itemCount[16] -= QuotientR
    if itemCount[16] < 0:
        itemCount[16] = 0
    else:
        pass

    RemainderQ = itemCount[16] % 3
    QuotientQ = itemCount[16] // 3

    RemainderU = itemCount[20] % 3
    QuotientU = itemCount[20] // 3
    itemCount[20] -= QuotientR
    if itemCount[20] < 0:
        itemCount[20] = 0
    else:
        pass

    RemainderV130 = itemCount[21] % 3
    QuotientV130 = itemCount[21] // 3
    RemainderV90 = RemainderV130 % 2
    QuotientV90 = RemainderV130 // 2

    # Output

    print(itemCount)
    finalPriceCompound = []
    finalPriceCompound.append(
        QuotientA200 * priceDictList['A1'] + QuotientA150 * priceDict['A2'] + RemainderA150 * priceDict['A'])
    finalPriceCompound.append(QuotientB * priceDict['B1'] + RemainderB * priceDict['B'])
    finalPriceCompound.append(
        QuotientH80 * priceDict['H1'] + QuotientH45 * priceDict['H2'] + RemainderH45 * priceDict['H'])
    finalPriceCompound.append(QuotientK * priceDict['K1'] + RemainderK * priceDict['K'])
    finalPriceCompound.append(QuotientP * priceDict['P1'] + RemainderP * priceDict['P'])
    finalPriceCompound.append(QuotientQ * priceDict['Q1'] + RemainderQ * priceDict['Q'])
    finalPriceCompound.append(QuotientV130 * priceDict['V1'] + QuotientV90 * priceDict['V2'] + RemainderV90 * priceDict['V'])

    finalPriceNoCompound = []
    for item in skuList:
        if item in ['A', 'B', 'H', 'K', 'P', 'Q', 'V']:
            pass
        else:
            finalPriceNoCompound.append(itemCount[skuList.index(item)] * priceDictList[skuList.index(item)[1]])

    finalPrice = sum(finalPriceNoCompound) + sum(finalPriceCompound)

    return finalPrice


