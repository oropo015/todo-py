import PySimpleGUI as sg
from  function import make_achieve as mk

label1 = sg.Text("Source Folder:    ")
t_box1 = sg.InputText()
choose1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Destination Folder:")
t_box2 = sg.InputText()
choose2 = sg.FolderBrowse("Choose")

compress = sg.Button("Compress")
window = sg.Window("Compressor", [[label1, t_box1, choose1], [label2, t_box2, choose2], [compress]])
while True:
    event, value = window.read()
    print(event)
    print(value)
    filepaths = value[0].split(";")
    dest = value[1]
    mk(filepaths, dest)


window.close()