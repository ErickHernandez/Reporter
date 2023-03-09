import os
import tarfile


def read_text_file(filepath: str) -> str:
    try:
        f = open(filepath, "r")
        text = f.read()
    except FileNotFoundError as e:
        print("File '{}' not found.".format(filepath))
        exit()

    return text


def create_folder(directory):
    parent_directory = ""
    path = os.path.join(parent_directory, directory)

    if os.path.exists(path):
        return

    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
        exit()


def compress_folder(filepath: str, output_filename: str):
    if not os.path.exists(filepath):
        print("Folder not found")
        exit()

    files = os.listdir(filepath)

    if len(files) == 0:
        return

    with tarfile.open(output_filename, "w:gz") as tar:
        for file in files:
            tar.add(filepath + "/" + file)


def file_exists(filepath: str):
    return os.path.exists(filepath)
