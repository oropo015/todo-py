import PySimpleGUI as sg
import function as fc

label = sg.Text("Enter your todo: ")
t_box = sg.InputText(tooltip="Enter a todo", key="todo")
Add = sg.Button("Add")
todo_list = sg.Listbox(values=fc.get_todos(), key="todos",
                       enable_events=True, size=(45, 10))
edit_list = sg.Button("Edit")
window = sg.Window("To-Do App", layout=[[label], [t_box, Add], [todo_list, edit_list]])

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = fc.get_todos()
            new_todo = values["todo"] + "\n"
            print(new_todo)
            todos.append(new_todo)
            fc.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            todos = fc.get_todos()
            new_edit = values["todo"] + "\n"
            print(todo_to_edit)
            index = todos.index(todo_to_edit)
            todos[index] = new_edit
            fc.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
    print(event)
    print(values)

window.close()
