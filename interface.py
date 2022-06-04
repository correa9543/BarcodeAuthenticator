
from multiprocessing import Event
from time import sleep
import PySimpleGUI as sg
import openAndSearchFile as oas
import time

sg.theme('Dark Grey 13')

inputFont = ("Arial, 15")
headerFont = ("Arial, 20")

addLayout = [[sg.Text('', font=headerFont, justification="c", key="addResultText")],
          [sg.Text('Enter Barcode To Add:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont, do_not_clear=False)],
          [sg.OK(size=(15,1)), sg.Exit(size=(15,1))]]

searchLayout = [[sg.Text('', font=headerFont, justification="c", key="resultText")],
    [sg.Text('Enter Barcode To Search:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont, do_not_clear=False)],
          [sg.OK(size=(15,1)), sg.Exit(size=(15,1))]]

removeLayout = [[sg.Text('', font=headerFont, justification="c", key="removeResultText")],
    [sg.Text('Enter Barcode To Remove:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont, do_not_clear=False)],
          [sg.OK(size=(15,1)), sg.Exit(size=(15,1))]]

# layout = [[sg.Radio('Add Item', "RADIO1", default=False, key="add", font=inputFont)],
#           [sg.Radio('Search Item', "RADIO1", default=False, key="search", font=inputFont)],
#           [sg.OK(size=(15,1),key="ok")]]

tabgrp = [[sg.TabGroup([[sg.Tab('Add Item', addLayout,border_width =10,
                                tooltip='Personal details', element_justification= 'center' , key= 'add'),
                    sg.Tab('Search Item', searchLayout, element_justification= 'center', key='search'), 
                    sg.Tab('Remove Item', removeLayout, element_justification= 'center', key='remove')]])]] 

window = sg.Window('Willow Sound System', tabgrp, margins=(100,100))

oas.beginModule()
# oas.printBarCodes()

while True:
    barcordeScanned = False
    barCodePresent = False


    event,values = window.read()


    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    else:
        # sleep(3)
        print("barcode has been entered")
        print(values)
        barcordeScanned = True
    
    if values[3] == 'add' and event == 'OK':
        addResult = oas.addBarcodeToList(values[0])

        if addResult == True:
            oas.putBarcodesInFile()
            window['addResultText'].update('Item ' + values[1] +  ' was added to the file!')
            window['addResultText'].update(background_color="#006400", text_color="#FFF")


        else:
            window['addResultText'].update('Item ' + values[1] +  ' is already in the file!')


    
    if event == 'OK' and values[3] == 'search':
        if values[1] != '':
            barCodePresent = oas.lookForBarCode(values[1])
            if barCodePresent == True:
                window['resultText'].update('Item ' + values[1] +  ' was purchased here!')
                window['resultText'].update(background_color="#006400")

                # window['resultText'].update('')
                # window['resultText'].update('') 
        

            else:
                window['resultText'].update('Item ' + values[1] + ' was NOT purchased here!')
                window['resultText'].update(background_color="#BF0000")

                # window['resultText'].update('')    
        else:
            window['resultText'].update("No barcode was entered.")

    if event == 'OK' and values[3] == 'remove':
        if values[2] != '':
            barCodePresent = oas.removeBarCode(values[2])
            if barCodePresent == True:
                oas.putBarcodesInFile()
                window['removeResultText'].update('Item ' + values[2] +  ' was removed from the file!')
                # window['resultText'].update('')
                # window['resultText'].update('') 
        

            else:
                window['removeResultText'].update('Item ' + values[2] + ' is not in the file!')
                # window['resultText'].update('')    
        else:
            window['removeResultText'].update("No barcode was entered.")


window.close()




