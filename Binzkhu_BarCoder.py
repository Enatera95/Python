import PySimpleGUI as sg
import pyautogui
from barcode import EAN13
from tkinter.filedialog import askdirectory


sg.theme('DarkAmber')
#Window and textfields
layout = [
        [sg.Text('NOTE: Only 12 digit numbers are allowed in the bar code field.')],
        [sg.Text('Item name:'), sg.InputText(key='tfield')],
        [sg.Text('Bar-code number:'), sg.Multiline(size=(40, 5), key='textbox')],
            [sg.Button('Generate Barcode')],
            #[sg.Text('NOTE: Only numbers are allowed in the barcode field.')],
            [sg.Text('')],
            [sg.Text('Developed by Datec (PNG) Software Team')]
            ]

window = sg.Window('Binzkhu Barcode Generator', layout, margins=(10, 10)).Finalize()

while True:
    event, values = window.read()
    if event in (None, 'Close Window'): 
        break

    path = askdirectory()+'/'
    
    filename = values['tfield']
    number = values['textbox']
    if(number.isdigit() and len(number) >= 12 and path != "" and filename !=""):
    	my_code = EAN13(number)

    	my_code.save(path+filename)
    	pyautogui.alert('Barcode for '+filename+' generated!', "Success")
    else:
    	pyautogui.alert('Please enter all information! NOTE: Only numbers are allowed in the barcode field.', "Wrong Input")
window.close()
