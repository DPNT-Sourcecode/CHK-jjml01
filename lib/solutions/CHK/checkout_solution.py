# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Initialisation, input handling



    skuList = list(map(chr, range(65, 91)))
    skuListNoOffer = []
    for items in skuList:
        if items in ['A', 'B', 'H', 'K', 'P', 'Q', 'V']:
            pass
        else:
            skuListNoOffer.append(items)

    itemList = [x for x in skus]
    print(itemList)
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
    initialCount = [sum(x) for x in itemBreakdown]
    itemCountInitial = list(zip(skuList,initialCount))
    itemCount = [list(x) for x in itemCountInitial]
    print(itemCount)

    # Price dictionary
    priceDict = [
        ('A',50),
        ('B',30),
        ('C',20),
        ('D',15),
        ('E',40),
        ('F',10),
        ('G',20),
        ('H',10),
        ('I',35),
        ('J',60),
        ('K',70),
        ('L',90),
        ('M',15),
        ('N',40),
        ('O',10),
        ('P',50),
        ('Q',30),
        ('R',50),
        ('S',20),
        ('T',20),
        ('U',40),
        ('V',50),
        ('W',20),
        ('X',17),
        ('Y',20),
        ('Z',21),
        ('A1',200),
        ('A2',130),
        ('B1',45),
        ('H1',80),
        ('H2',45),
        ('K1',120),
        ('P1',200),
        ('Q1',80),
        ('V1',130),
        ('V2',90),
        ('MO',45)
    ]


    DictIndexT, DictValueT = zip(*priceDict)
    DictIndex = list(DictIndexT)
    DictValue = list(DictValueT)
    print(priceDict)
    print(DictIndex,DictValue)
    # Offers

    RemainderA200 = itemCount[0][1] % 5
    QuotientA200 = itemCount[0][1] // 5
    RemainderA150 = RemainderA200 % 3
    QuotientA150 = RemainderA200 // 3

    RemainderE = itemCount[4][1] % 2
    QuotientE = itemCount[4][1] // 2
    itemCount[1][1] -= QuotientE
    if itemCount[1][1] < 0:
        itemCount[1][1] = 0
    else:
        pass

    RemainderB = itemCount[1][1] % 2
    QuotientB = itemCount[1][1] // 2

    RemainderF = itemCount[5][1] % 3
    QuotientF = itemCount[5][1] // 3
    itemCount[5][1] -= QuotientF

    RemainderH80 = itemCount[7][1] % 10
    QuotientH80 = itemCount[7][1] // 10
    RemainderH45 = RemainderH80 % 5
    QuotientH45 = RemainderH80 // 5

    RemainderK = itemCount[10][1] % 2
    QuotientK = itemCount[10][1] // 2

    RemainderN = itemCount[13][1] % 3
    QuotientN = itemCount[13][1] // 3
    itemCount[12][1] -= QuotientN
    if itemCount[12][1] < 0:
        itemCount[12][1] = 0
    else:
        pass

    RemainderP = itemCount[15][1] % 5
    QuotientP = itemCount[15][1] // 5

    RemaindeR = itemCount[17][1] % 3
    QuotientR = itemCount[17][1] // 3
    itemCount[16][1] -= QuotientR
    if itemCount[16][1] < 0:
        itemCount[16][1] = 0
    else:
        pass

    RemainderQ = itemCount[16][1] % 3
    QuotientQ = itemCount[16][1] // 3

    RemainderU = itemCount[20][1] % 4
    QuotientU = itemCount[20][1] // 4
    itemCount[20][1] -= QuotientU
    if itemCount[20][1] < 0:
        itemCount[20][1] = 0
    else:
        pass

    RemainderV130 = itemCount[21][1] % 3
    QuotientV130 = itemCount[21][1] // 3
    RemainderV90 = RemainderV130 % 2
    QuotientV90 = RemainderV130 // 2

    multiOffer = sum(itemCount[skuList.index(x)][1] for x in ['S','T','X','Y','Z'])
    multiOfferRemainder = multiOffer % 3
    multiOfferQuotient = multiOffer // 3
    totalLoss = multiOfferQuotient * 3
    print('initial total loss',totalLoss)
    while totalLoss > 0:
        for item in itemCount:
            for character in ['Z','Y','T','S','X']:


                if skuList[itemCount.index(item)] == character:
                    if totalLoss == 0:
                        break
                    if itemCount[itemCount.index(item)][1] > 0:
                        itemCount[itemCount.index(item)][1] -= 1
                        totalLoss -= 1
                    else:
                        pass

                    print('total loss',totalLoss)
                else:
                    pass


    # Output

    print(itemCount)

    finalPriceCompound = []

    finalPriceCompound.append(QuotientA200 * DictValue[DictIndex.index('A1')] + QuotientA150 * DictValue[DictIndex.index('A2')] + RemainderA150 * DictValue[DictIndex.index('A')])
    finalPriceCompound.append(QuotientB * DictValue[DictIndex.index('B1')] + RemainderB * DictValue[DictIndex.index('B')])
    finalPriceCompound.append(QuotientH80 * DictValue[DictIndex.index('H1')] + QuotientH45 * DictValue[DictIndex.index('H2')] + RemainderH45 * DictValue[DictIndex.index('H')])
    finalPriceCompound.append(QuotientK * DictValue[DictIndex.index('K1')] + RemainderK * DictValue[DictIndex.index('K')])
    finalPriceCompound.append(QuotientP * DictValue[DictIndex.index('P1')] + RemainderP * DictValue[DictIndex.index('P')])
    finalPriceCompound.append(QuotientQ * DictValue[DictIndex.index('Q1')] + RemainderQ * DictValue[DictIndex.index('Q')])
    finalPriceCompound.append(QuotientV130 * DictValue[DictIndex.index('V1')] + QuotientV90 * DictValue[DictIndex.index('V2')] + RemainderV90 * DictValue[DictIndex.index('V')])
    finalPriceCompound.append(multiOfferQuotient * DictValue[DictIndex.index('MO')])
    print('multioffer quotient',multiOfferQuotient,DictValue[DictIndex.index('MO')])
    finalPriceNoCompound = []
    print(finalPriceCompound)
    for item in skuList:

        if item in skuListNoOffer:
            finalPriceNoCompound.append(itemCount[skuList.index(item)][1] * DictValue[skuList.index(item)])

        else:
            pass


    print(finalPriceNoCompound)
    finalPrice = sum(finalPriceNoCompound) + sum(finalPriceCompound)

    return finalPrice
