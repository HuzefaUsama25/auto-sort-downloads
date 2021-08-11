import os


def get_files():
    all_items = os.listdir()
    files = [i for i in all_items if "." in i]
    return files


def get_file_extension(file):
    extension = file.split(".")[-1]
    return extension


def get_file_url(file):
    os.popen(f"powershell Get-Content {file} -Stream Zone.Identifier").read().split(
        "\n")[-2].replace("HostUrl=", "")


def move_files():
    files = get_files()
    for file in files:
        extension = get_file_extension(file)
        url = get_file_url(file)
