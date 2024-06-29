import PySimpleGUI as sg
import function as fc

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

window = sg.Window("To Do App", layout=[[label], [t_box, Add], [edit_list, Edit, Delete]])
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todo = value['todo'] + "\n"
            todos = fc.get_todos()
            todos.append(todo)
            fc.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            value_to_edit = value['todos'][0]
            todos = fc.get_todos()
            to_edit = value['todo'] + "\n"
            index = todos.index(value_to_edit)
            todos[index] = to_edit
            fc.write_todos(todos)
            window['todos'].update(values=todos)
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
        case sg.WIN_CLOSED:
            break

window.close()