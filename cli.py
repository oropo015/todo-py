from function import get_todos, write_todos
import time


now = time.strftime("%b - %d, %Y %H:%M:%S")
print("The time is: " + now)

while True:
    todo = input("Select an option: a = add, d = delete, e = edit, s = show, x = exit: ")
    todo = todo.strip()
    try:
        if todo.startswith("add"):
            add_task = todo[4:]
            todos = get_todos()
            todos.append(add_task + "\n")
            write_todos(todos)
        elif todo.startswith("show"):
            todos = get_todos()
            new_todos = []
            [new_todos.append(x.strip("\n")) for x in todos]
            for i, x in enumerate(new_todos):
                print(f"{i+1}", "->", f"{x}")
        elif todo.startswith("delete"):
            delete_item = int(input("Enter the number of item to be deleted: "))
            try:
                todos = get_todos()
                item = todos[delete_item]
                todos.remove(item)
                print([x.strip("\n") for x in todos])
            except IndexError:
                print("No index with the stated number")
                continue
        elif todo.startswith("edit"):
            try:
                edit_item = int(todo[5])
                todos = get_todos()
                new_item = todo[7:]
                todos[edit_item] = new_item
                print([x.strip("\n") for x in todos])
            except IndexError:
                print("Incomplete input")
                continue
        elif todo.startswith("exit"):
            print("Exiting.........")
            break
    except ValueError:
        print("Invalid input")
        continue


