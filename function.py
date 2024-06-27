def get_todos():
    with open("todo.txt", "r") as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_write):
    with open("todo.txt", "w") as file:
        todos_list = file.writelines(todos_write)