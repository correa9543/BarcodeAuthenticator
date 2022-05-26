
from multiprocessing import Event
import PySimpleGUI as sg
import openAndSearchFile as oas

sg.theme('Dark Grey 13')

inputFont = ("Arial, 15")
headerFont = ("Arial, 20")

addLayout = [[sg.Text('Enter Barcode To Add:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont)],
          [sg.OK(size=(15,1)), sg.Cancel(size=(15,1))]]

searchLayout = [[sg.Text('', font=headerFont, justification="c", key="resultText")],
    [sg.Text('Enter Barcode To Search:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont), sg.FileBrowse(size=(15,1))],
          [sg.OK(size=(15,1)), sg.Cancel(size=(15,1))]]

# layout = [[sg.Radio('Add Item', "RADIO1", default=False, key="add", font=inputFont)],
#           [sg.Radio('Search Item', "RADIO1", default=False, key="search", font=inputFont)],
#           [sg.OK(size=(15,1),key="ok")]]

tabgrp = [[sg.TabGroup([[sg.Tab('Add Item', addLayout,border_width =10,
                                tooltip='Personal details', element_justification= 'center' , key= 'add'),
                    sg.Tab('Search Item', searchLayout, element_justification= 'center', key='search')]])]] 

window = sg.Window('Willow Sound System', tabgrp, margins=(100,100))

oas.beginModule()
oas.printBarCodes()
barCodePresent = False

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    else:
        print("barcode has been scanned")
        print(values)

    if values[2] == 'add' and event == 'OK':
        oas.addBarcodeToList(values[0])
        oas.putBarcodesInFile()

    
    if values[2] == 'search' and event == 'OK':
        barCodePresent = oas.lookForBarCode(values[1])
        if barCodePresent == True:
            window['resultText'].update('Item was purchased here!')
        else:
            window['resultText'].update('Item was NOT purchased here!')



window.close()




