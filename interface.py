
from multiprocessing import Event
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

inputFont = ("Arial, 15")
headerFont = ("Arial, 20")

addLayout = [[sg.Text('Enter Barcode To Add:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont), sg.FileBrowse(size=(15,1))],
          [sg.OK(size=(15,1)), sg.Cancel(size=(15,1))]]

searchLayout = [[sg.Text('Enter Barcode To Search:', font=headerFont, justification="c")],
          [sg.Input(font=inputFont), sg.FileBrowse(size=(15,1))],
          [sg.OK(size=(15,1)), sg.Cancel(size=(15,1))]]

# layout = [[sg.Radio('Add Item', "RADIO1", default=False, key="add", font=inputFont)],
#           [sg.Radio('Search Item', "RADIO1", default=False, key="search", font=inputFont)],
#           [sg.OK(size=(15,1),key="ok")]]

tabgrp = [[sg.TabGroup([[sg.Tab('Add Item', addLayout,border_width =10,
                                tooltip='Personal details', element_justification= 'center' , key= 'add'),
                    sg.Tab('Search Item', searchLayout, element_justification= 'center', key='search')]])]] 

window = sg.Window('Willow Sound System', tabgrp, margins=(100,100))

# event, values = window.read()

while True:
    event,values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    else:
        print("barcode has been scanned")
        print(values)
# while True:
#     # event,values = window.read()

#     if event == sg.WINDOW_CLOSED or event == "Exit":
#         break
#     elif values["add"] == True and event == "OK":
#         window = sg.Window('Willow Sound System', addLayout, margins=(100,100))
#         event, values = window.read()
#         values["add"] = False
#         break

#     else:
#         layout = searchLayout


window.close()

def addCode():
    return

