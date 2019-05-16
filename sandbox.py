import pathlib

from bullet import Bullet, Check, YesNo, Input, VerticalPrompt, Numbers

import click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}")


def txt_headers():
    path_ = pathlib.Path.cwd() / "_z-shell.txt"

    with open(path_, mode="r") as fid:
        headers = [line.strip() for line in fid if line.startswith("#")]

    print(headers)


def unique_path(directory, name_pattern):
    counter = 0

    while True:
        counter += 1
        path = directory / name_pattern.format(counter)

        if not path.exists():
            return path


def rename():
    # Function to rename multiple files
    i = 0
    media_folder = pathlib.Path(r"/Users/Developer")

    for filename in os.listdir(media_folder):
        destination = "renamed-file" + str(i) + ".pdf"
        src_root = str(media_folder) + "/" + filename

        # rename() function will rename all the files
        os.rename(src_root, destination)
        i += 1


def tree(directory):
    print(f"+ {directory}")

    for path_ in sorted(directory.rglob("*")):
        depth = len(path_.relative_to(directory).parts)
        spacer = "\t" * depth
        print(f"{spacer} + {path_.name}")


if __name__ == "__main__":
    path_ = unique_path(pathlib.Path.cwd(), "test{:03d}.txt")
    print(path)
    hello()
