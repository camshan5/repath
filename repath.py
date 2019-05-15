# Analyze Files and Paths
from pathlib import Path, PurePath
from bullet import Bullet, VerticalPrompt, ScrollBar


def find_dir():
    # py_path = Path.home() / "Developer" / "Language" / "Python"

    current_dir = Path.cwd()
    if current_dir.is_dir():

        # list of all files in directory
        path_list = []
        for p in current_dir.iterdir():

            # string representation of path names
            p = PurePath(p).name

            # append only .py files to list
            if PurePath(p).suffix == ".py":
                path_list.append(p)

        print(path_list)

        cli = VerticalPrompt(
            [Bullet("Please select a file or path", choices=path_list, bullet="→")],
            spacing=1,
        )

        result = cli.launch()

        print(f"You selected: {result}")

    else:
        print("Directory does not exist")


#
# def tree(directory):
#     print(f"+ {directory}")
#
#     for path_ in sorted(directory.rglob("*")):
#         depth = len(path_.relative_to(directory).parts)
#         spacer = "\t" * depth
#         print(f"{spacer} + {path_.name}")


# Driver Code
if __name__ == "__main__":
    # tree(Path.cwd())
    find_dir()
