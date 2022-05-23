from openpyxl import Workbook
import os.path



def createWorkbookPath(path):
    workbook = Workbook()
    workbook.save(path)

def grabFileBarcodes(file):

    # return the datastructure with the bar codes
    return 

# Change the path name to see if the file exists in the given path, if it doesnt, create the file
if os.path.isfile('filename.txt'):
    grabFileBarcodes("dummy.txt")
    print ("File exist")
else:
    createWorkbookPath("dummy.txt")
