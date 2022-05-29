

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    itemList = [x for x in skus]
    As = [x == 'A' for x in itemList]
    Bs = [x == 'B' for x in itemList]
    Cs = [x == 'C' for x in itemList]
    Ds = [x == 'D' for x in itemList]

    priceList = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15

    }








