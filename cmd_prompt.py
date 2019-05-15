import pathlib

from bullet import Bullet, Check, YesNo, Input, VerticalPrompt, Numbers


def path_prompt(obj, *args, **kwargs):

    cli = VerticalPrompt(
        [
            Input("Enter your path"),
            Bullet(
                "Select the path you wish to search",
                choices=["C++", "Python", "Javascript", "Not here!"],
            ),
        ],
        spacing=1,
    )
    result = cli.launch()
    print(result)



def txt_headers():
    path_ = pathlib.Path.cwd() / "_z-shell.txt"

    with open(path_, mode="r") as fid:
        headers = [line.strip() for line in fid if line.startswith("#")]

    print(headers)


# def unique_path(directory, name_pattern):
#     counter = 0
#     while True:
#         counter += 1
#         path = directory / name_pattern.format(counter)
#         if not path.exists():
#             return path
#
#
# path = unique_path(pathlib.Path.cwd(), "test{:03d}.txt")

# Function to rename multiple files
def main():
    i = 0

    media_folder = pathlib.Path(r"/Users/Developer")

    for filename in os.listdir(media_folder):
        destination = "renamed-file" + str(i) + ".pdf"
        src_root = str(media_folder) + "/" + filename

        # rename() function will rename all the files
        os.rename(src_root, destination)
        i += 1