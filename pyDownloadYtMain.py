from cgitb import text
from importlib.metadata import metadata
from pydoc import visiblename
from subprocess import call
from tokenize import String
import PySimpleGUI as sg
import urllib.request
import urllib.parse
import os

layout = [[sg.Text('Nom de la cançó')],[sg.Input('', enable_events=True,  key='name', )],[sg.Text("Descarregant...", visible=False, key='status')], [sg.Submit('Descarregar')],[sg.Submit("Obrir", visible=False, metadata="")]]
window = sg.Window("Descarregar cançons de YouTube", layout, icon='youtube-icon-ico-5.ico')


def open_explorer(path):
    os.system(f"explorer.exe {path}")
while True:             
    event, values = window.read()
    if callable(event):
        event()
    elif event == 'Descarregar':
        foldername = sg.PopupGetFolder('', no_window=True)
        window['Obrir'].update(visible=False)
        window['status'].update(visible=True)
        window['status'].update('Descarregant...')
        window.refresh()
        parsed = urllib.parse.quote(values['name'])
        url = 'http://localhost:8000/apiDownload?name='+parsed
        urllib.request.urlretrieve(url, foldername+'/'+values['name']+'.mp3')
        fullPath = foldername+'/'+values['name']+'.mp3'
        open_explorer(foldername)
        window['status'].update(f'Descarregat a {fullPath} correctament.')
        window['Obrir'].update(visible=True)
        window.refresh()
    elif event == sg.WIN_CLOSED:    
        break

window.close()