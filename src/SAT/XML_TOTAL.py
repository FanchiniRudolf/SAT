import xml.dom.minidom
import os
from tkinter.filedialog import askdirectory

TAXRATE = 0.16


def getAmounts(xmlPathName):
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(xmlPathName)
    collection = DOMTree.documentElement

    tax = getAttribute("cfdi:Impuestos", "TotalImpuestosTrasladados", collection)
    price = tax/TAXRATE
    print("Precio:", price, "Impuesto:", tax)
    return price, tax

def getAttribute(tag, attribute, collection):
    elementTag = collection.getElementsByTagName(tag)[-1]
    if (elementTag.hasAttribute(attribute)):
       return float(elementTag.getAttribute(attribute))

def main():
    totalPrice, taxTotal = 0.0, 0.0

    # shows dialog box and return the path
    folderPath = askdirectory(title='Select Folder')+"/"
    print(folderPath)
    files = os.listdir(folderPath)

    for file in files:
        if (".xml" in file):
            print(file)
            totalPrice, taxTotal = map(float.__add__,
                                       (totalPrice, taxTotal), getAmounts(folderPath+file))
            print("Precio total:", totalPrice, "Impuesto total:", taxTotal)
    print("Precio total:", totalPrice, "Impuesto total:", taxTotal)

if __name__ == '__main__':
    main()
