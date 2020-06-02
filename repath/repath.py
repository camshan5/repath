import os
from os import system, name, walk

from pathlib import Path, PurePath
from bullet import Bullet, VerticalPrompt, ScrollBar


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(os.name is 'posix')
    else:
        _ = system("clear")


cwd = Path.cwd()

selected_files = []


def build_path(*args, **kwargs):

    n = 0
    key = n + 1
    for item in selected_files:

        d = {key: item}

    print(d)

    # path_list = []

    # py_path = Path.home() / f"{}"

    # for p in cwd.iterdir():
    #     # The file extension of the final component, if any -> .py

    #     parts = PurePath(p).parts
    #     print(parts)

    # print(py_path)


def bullet_prompt(path_list):

    cli = VerticalPrompt(
        [Bullet("Select a file or path", choices=path_list, bullet="→")], spacing=1
    )

    result = cli.launch()

    result_item = result.pop()

    returned_item = result_item[1]

    print(f"You selected: {returned_item}")

    selected_files.append(returned_item)


def list_sfx():
    path_list = []

    for p in cwd.iterdir():
        # The file extension of the final component, if any -> .py
        sfx = PurePath(p).suffix
        parts = PurePath(p).parts

        # if suffix not an empty string, append to list
        if sfx != "":
            path_list.append(sfx)

    return path_list


def find_ext():
    sfx_list = list(dict.fromkeys(list_sfx()))
    cli = Bullet(
        prompt="\nSelect a file extension you are looking for: ",
        choices=sfx_list,
        bullet="→",
    )
    result = cli.launch()

    print(f"\nYou selected the '{result}' file suffix\n ")

    return result


def find_dir():
    clear()
    file_ext = find_ext()
    current_dir = Path.cwd()

    if current_dir.is_dir():
        # list of all files in directory
        path_list = []

        for p in current_dir.iterdir():
            # string representation of path names
            p = PurePath(p).name

            # append selected files from find_ext() to list
            if PurePath(p).suffix == file_ext:
                path_list.append(p)

        bullet_prompt(path_list)

    else:
        print("Directory does not exist")


def list_files(startpath):
    IGNORE_LIST = [".git", ".vscode", ".gitignore"]

    for root, dirs, files in walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        print("{}{}/".format(indent, PurePath(root).name))

        subindent = " " * 4 * (level + 1)

        for f in files:
            print("{}{}".format(subindent, f))


if __name__ == "__main__":
    find_dir()
    # p = Path.cwd()
    # list_files(str(p))

    build_path()
