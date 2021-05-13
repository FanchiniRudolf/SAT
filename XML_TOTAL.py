import xml.dom.minidom
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory




def getAmounts(xmlPathName):
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse(xmlPathName)
    collection = DOMTree.documentElement

    price = getAttribute("cfdi:Concepto", "Importe", collection)
    tax = getAttribute("cfdi:Traslado", "Importe", collection)

    return price, tax

def getAttribute(tag, attribute, collection):
    elementTag = collection.getElementsByTagName(tag).item(0)
    if (elementTag.hasAttribute(attribute)):
       return float(elementTag.getAttribute(attribute))

def main():
    totalPrice, taxTotal = 0.0, 0.0

    # shows dialog box and return the path
    folderPath = askdirectory(title='Select Folder')+"/"
    files = os.listdir(folderPath)

    for file in files:
        if (".xml" in file):
            totalPrice, taxTotal = map(float.__add__,
                                       (totalPrice, taxTotal), getAmounts(folderPath+file))
    print("Precio:", totalPrice, "Impuesto:", taxTotal)

if __name__ == '__main__':
    main()
    
