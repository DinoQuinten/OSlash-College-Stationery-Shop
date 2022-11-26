from sys import argv

# price list
priceList = {"TSHIRT": (1000, 0.10), "JACKET": (2000, 0.05), "CAP": (500, 0.20),
             "NOTEBOOK": (200, 0.20), "PENS": (300, 0.10), "MARKERS": (500, 0.05)}

purchasedItems = {}


def billAfterTax(amount):
    amountFinal = amount * 0.10
    amountTotal = amount + amountFinal
    return amountTotal


def outPrint():
    totalValue = 0
    totalDiscount = 0
    if purchasedItems["TotalPrice"] <= 999:
        print("TOTAL_DISCOUNT {:0.2f}".format(0))
        am = billAfterTax(purchasedItems["TotalPrice"])
        print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))

    elif purchasedItems["TotalPrice"] >= 1000 and purchasedItems["TotalPrice"] <= 2999:
        for keys in purchasedItems:
            if keys != "TotalPrice":
                cValue = purchasedItems[keys] * priceList[keys][0]
                discount = cValue * priceList[keys][1]
                totalValue += cValue
                totalDiscount += discount
        for keys in purchasedItems:
            if keys == "TotalPrice":
                tfvalue = totalValue - totalDiscount
                print("TOTAL_DISCOUNT {:0.2f}".format(totalDiscount))
                am = billAfterTax(tfvalue)
                print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))


    elif purchasedItems["TotalPrice"] >= 3000:
        for keys in purchasedItems:
            if keys != "TotalPrice":
                cValue = purchasedItems[keys] * priceList[keys][0]
                discount = cValue * priceList[keys][1]
                totalValue += cValue
                totalDiscount += discount

        for keys in purchasedItems:
            if keys == "TotalPrice":
                tfvalue = totalValue - totalDiscount
                discountValue = tfvalue * 0.05
                disTotal = totalDiscount + discountValue
                finaleValue = tfvalue - discountValue

                print("TOTAL_DISCOUNT {:0.2f}".format(disTotal))
                am = billAfterTax(finaleValue)
                print("TOTAL_AMOUNT_TO_PAY {:0.2f}".format(am))


def main():
    # Sample code to read inputs from the file
    cartValue = 0
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    dataFile = open(file_path, 'r')
    lines = dataFile.readlines()
    for line in lines:
        data = line.split()
        if data[0] == "ADD_ITEM":
            if data[1] == "TSHIRT" or data[1] == "JACKET" or data[1] == "CAP":
                if int(data[2]) <= 2:
                    purchasedItems[data[1]] = int(data[2])
                    temp = int(data[2]) * priceList[data[1]][0]
                    cartValue += temp
                    print("ITEM_ADDED")
                else:
                    print("ERROR_QUANTITY_EXCEEDED")
            elif data[1] == "NOTEBOOK" or data[1] == "PENS" or data[1] == "MARKERS":
                if int(data[2]) <= 3:
                    purchasedItems[data[1]] = int(data[2])
                    temp = int(data[2]) * priceList[data[1]][0]
                    cartValue += temp
                    print("ITEM_ADDED")
                else:
                    print("ERROR_QUANTITY_EXCEEDED")
            purchasedItems["TotalPrice"] = cartValue

        elif data[0] == "PRINT_BILL":
            outPrint()


if __name__ == "__main__":
    main()
