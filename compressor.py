import PySimpleGUI as sg

label1 = sg.Text("Source Folder     :")
t_box1 = sg.InputText()

label2 = sg.Text("Destination Folder:")
t_box2 = sg.InputText()

compress = sg.Button("Compress")
window = sg.Window("Compressor", [[label1, t_box1], [label2, t_box2], [compress]])
window.read()
window.close()