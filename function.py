import zipfile
import pathlib


def get_todos():
    with open("todo.txt", "r") as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_write):
    with open("todo.txt", "w") as file:
        todos_list = file.writelines(todos_write)


def make_achieve(filepaths_, dest_):
    dest_dir = pathlib.Path(dest_, "dest.zip")
    with zipfile.ZipFile(dest_dir, 'w') as achieve:
        for file in filepaths_:
            file = pathlib.Path(file)
            achieve.write(file, arcname=file.name)


if __name__ == '__main__':
    filepaths=["a.txt", "b.txt", "c.txt"]
    dest = "dest"
    make_achieve(filepaths, dest)