import PySimpleGUI as sg
from function import un_achieve

label1 = sg.Text("Source File:           ",key="Label")
t_box1 = sg.InputText(tooltip="Select file to decompress")
choose1 = sg.FileBrowse(key="choose_file")

label2 = sg.Text("Destination Folder:",key="Label")
t_box2 = sg.InputText(tooltip="Select file to decompress")
choose2 = sg.FolderBrowse(key="choose_file")

Decompress = sg.Button("Decompress")
output = sg.Text("", key="output")
Exit = sg.Button("Exit")

window = sg.Window("Decompressor", [[label1, t_box1, choose1],
                                    [label2, t_box2, choose2],[Decompress, output]], font=("Helvetica", 15))

while True:
    event, value = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
    try:
        source = value[0]
        destination = value[1]
        un_achieve(source, destination)
        window['output'].update("File has been uncompressed")
    except FileNotFoundError:
        sg.popup("File Not Selected")
        continue
window.close()
