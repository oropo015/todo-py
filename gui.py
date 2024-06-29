import PySimpleGUI as sg
import function as fc
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass

clock = sg.Text("", key='clock')
label = sg.Text("Enter your todo: ")
t_box = sg.InputText(tooltip="Todo here", key='todo')
Add = sg.Button("Add")
edit_list = sg.Listbox(
    values=fc.get_todos(),
    size=(45, 15),
    key='todos',
    enable_events=True
)
Edit = sg.Button("Edit")
Delete = sg.Button("Delete")
Exit = sg.Button("Exit")

window = sg.Window("To Do App", layout=[[clock],[label], [t_box, Add],
                    [edit_list, Edit, Delete],[Exit]],
                   font=("Helvetica", 15))
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(time.strftime("%b - %d, %Y %H:%M:%S"))
    match event:
        case sg.WIN_CLOSED:
            break
        case "Add":
            todo = value['todo'] + "\n"
            todos = fc.get_todos()
            todos.append(todo)
            fc.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                value_to_edit = value['todos'][0]
                todos = fc.get_todos()
                to_edit = value['todo'] + "\n"
                index = todos.index(value_to_edit)
                todos[index] = to_edit
                fc.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please enter a value")
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case "Delete":
            value_to_delete = value['todos'][0]
            print(value_to_delete)
            todos = fc.get_todos()
            #index = todos.index(value_to_edit)
            todos.remove(value_to_delete)
            fc.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break

window.close()