from urllib.robotparser import RobotFileParser
from numpy import equal
from openpyxl import Workbook
import os.path
import pandas as pd
from openpyxl import load_workbook



def createFile(path):
    workbook = Workbook()
    workbook.save(path)

# Grabbing the barcodes from the excel file
def grabFileBarcodes(filePath):
    wb = load_workbook(filePath)
    source = wb["Sheet"]
    for cell in source['1']:
        if cell.value != None:
            barcodes.append(cell.value)

def removeBarCode(barcode):

    if barcode not in barcodes:
        print("Barcode: ", barcode, " is not in the datasheet!")
    else:
        global barCodesListChanged
        barCodesListChanged = True
        barcodes.remove(barcode)
        print("Barcode: ", barcode, " has been removed!")


def addBarcodeToList(barcode):
    if barcode not in barcodes:
        global barCodesListChanged
        barCodesListChanged = True
        barcodes.append(barcode)
    else:
        print("Barcode: ",barcode, " already in data sheet")




def putBarcodesInFile():
    if barCodesListChanged:
        wb = load_workbook(filePath)
        ws = wb.active
        ws.delete_rows(1,2)
        ws.append(barcodes)
        wb.save(filename=filePath)
        print("File changed")
    else:
        print("file not changed")

# Change the path name to see if the file exists in the given path, if it doesnt, create the file
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
filePath = desktop + '/barcodes.xlsx'
barCodesListChanged = False
barcodes = []

if os.path.isfile(filePath):
    grabFileBarcodes(filePath)
    print ("File exists")
else:
    createFile(filePath)

# addBarcodeToList(999999999)
# addBarcodeToList(999999998)
# addBarcodeToList(999999997)
# addBarcodeToList(999999996)
removeBarCode(999999997)



putBarcodesInFile()
print(barcodes)

