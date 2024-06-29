import PySimpleGUI as sg
from  function import make_achieve as mk

label1 = sg.Text("Source Folder:    ")
t_box1 = sg.InputText()
choose1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Destination Folder:")
t_box2 = sg.InputText()
choose2 = sg.FolderBrowse("Choose")

compress = sg.Button("Compress")
output = sg.Text(key="output", text_color="green")
window = sg.Window("Compressor", [[label1, t_box1, choose1], [label2, t_box2, choose2], [compress, output]])
while True:
    event, value = window.read()
    filepaths = value[0].split(";")
    dest = value[1]
    mk(filepaths, dest)
    window['output'].update(value="Compression completed!")


window.close()