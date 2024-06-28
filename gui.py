import PySimpleGUI as sg

label = sg.Text("Enter your todo: ")
Add = sg.Button("Add")
window = sg.Window("To Do App", layout=[[label]])
window.read()
window.close()