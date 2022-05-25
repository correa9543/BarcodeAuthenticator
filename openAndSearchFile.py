from urllib.robotparser import RobotFileParser
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
        barcodes.append(cell.value)

def addBarcodeToList(barcode):
    barcodes.append(barcode)
    barCodesListChanged = True


def putBarcodesInFile():
    if barCodesListChanged:
        wb = load_workbook(filePath)
        ws = wb.active
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

addBarcodeToList(999999999)
putBarcodesInFile()
print(barcodes)

