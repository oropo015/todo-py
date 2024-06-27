import PySimpleGUI as sg

label = sg.Text("Enter your todo: ")
t_box = sg.InputText()
Add = sg.Button("Add")
window = sg.Window("To-Do App", layout=[[label], [t_box, Add]])
window.read()
window.close()