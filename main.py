import os
import time


def get_files(directory):
    all_items = os.listdir(directory)
    files = [i for i in all_items if "." in i]
    return files


def get_file_extension(file):
    extension = file.split(".")[-1]
    return extension


def get_file_url(file):
    raw_url = os.popen(
        f"powershell Get-Content 'Photos/{file}' -Stream Zone.Identifier").read()

    if "Error" in raw_url:
        return "other"

    else:
        url = raw_url.split("\n")[-2].replace("HostUrl=", "")
        domain = url.split(".")[1]
        return domain


def move_file_to_folder(file):
    file_folder_map = {
        "exe": "Applications & Games",
        "msi": "Setups",
        "png": "Photos",
        "jfif": "Photos",
        "jpg": "Photos",
        "jpeg": "Photos",
        "gif": "Photos",
        "tif": "Photos",
        "bmp": "Photos",
        "ico": "Photos",
        "svg": "Photos",
        "mp3": "Music",
        "wav": "Music",
        "wma": "Music",
        "aac": "Music",
        "ogg": "Music",
        "mp4": "Videos",
        "webm": "Videos",
        "mov": "Videos",
        "wmv": "Videos",
        "avi": "Videos",
        "mkv": "Videos",
        "m4v": "Videos",
        "mpg": "Videos",
        "mpeg": "Videos",
        "pdf": "Documents",
        "txt": "Documents",
        "doc": "Documents",
        "docx": "Documents",
        "ppt": "Documents",
        "pptx": "Documents",
        "html": "Documents",
        "csv": "Documents",
        "7z": "Compressed Files",
        "zip": "Compressed Files",
        "rar": "Compressed Files",

    }

    extension = get_file_extension(file)
    print(extension)

    folder_to_put_in = file_folder_map.get(extension)
    print(folder_to_put_in)

    if folder_to_put_in == None:
        folder_to_put_in = "UnIdentified"

    if folder_to_put_in not in os.listdir():
        os.mkdir(folder_to_put_in)

    os.system(f'move "{file}" "{folder_to_put_in}"')


def classify_photos_in_folder():
    # calssify photos according to source!
    photo_files = get_files("Photos")
    for file in photo_files:
        url = get_file_url(file)
        if url not in os.listdir("Photos"):
            os.mkdir(f"Photos/{url}")

        os.system(f'move "Photos\\{file}" "Photos\\{url}"')


def main():
    while True:
        time.sleep(10)
        all_files = get_files(None)

        try:
            all_files.remove("unconfirmed.crdownload")
            all_files.remove("Unconfirmed.crdownload")
            all_files.remove("main.py")
            all_files.remove("README.md")
            all_files.remove("desktop.ini")
            all_files.remove("cleandesk.exe")
        except Exception as e:
            print(e)
            continue

        for file in all_files:
            move_file_to_folder(file)
        classify_photos_in_folder()


if __name__ == "__main__":
    main()
