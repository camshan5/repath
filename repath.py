# Analyze Files and Paths
from pathlib import Path, PurePath
from bullet import Bullet, VerticalPrompt, ScrollBar


def list_suffix():
    # list file suffixes in path -> '.py'
    path_list = []

    cwd = Path.cwd()

    for p in cwd.iterdir():
        sfx = PurePath(p).suffix

        # if suffix not an empty string, append to list
        if sfx != "":
            path_list.append(sfx)

    return path_list


def find_ext():

    sfx_list = list(dict.fromkeys(list_suffix()))

    cli = Bullet(prompt="\nSelect a file extension: ", choices=sfx_list, bullet="→")

    result = cli.launch()

    print(f"\nYou selected: {result}\n")

    return result


def find_dir():
    # py_path = Path.home() / "Developer" / "Language" / "Python"

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

        cli = VerticalPrompt(
            [Bullet("Select a Path", choices=path_list, bullet="→")], spacing=1
        )

        result = cli.launch()

        print(f"You selected: {result}")

    else:
        print("Directory does not exist")


if __name__ == "__main__":
    find_dir()
