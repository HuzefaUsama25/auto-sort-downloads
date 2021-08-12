import os
import time

# get all the files present in your directory


def get_files(directory):
    all_items = os.listdir(directory)
    # get only files and ignore folders
    files = [i for i in all_items if "." in i]
    return files

# get the file extension i.e. .exe for a file


def get_file_extension(file):
    extension = file.split(".")[-1]
    return extension

# get the url from which the file was downloaded.
# refer to this for more info: https://pc.net/extensions/file/zone.identifier#:~:text=Zone%20identifier%20files%20are%20generated,meant%20to%20be%20opened%20directly.


def get_file_url(file):
    try:
        # get zone identifier.
        raw_url = os.popen(
            f"powershell Get-Content 'Photos/{file}' -Stream Zone.Identifier").read()

        print(raw_url)
        # clean the zone identifier to get url and clean it.
        url = raw_url.split("\n")[-2].replace("HostUrl=", "")
        # get the domain name of the url. such as: google, pinterest, etc.
        domain = url.split(".")[1]
        return domain
    except Exception as e:
        print(e)


def move_file_to_folder(file):
    # file extensions to associate with folders
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
        folder_to_put_in = "Unidentified"

    if folder_to_put_in not in os.listdir():
        os.mkdir(folder_to_put_in)

    os.system(f'move "{file}" "{folder_to_put_in}"')


def classify_photos_in_folder():
    # calssify photos according to source url.
    photo_files = get_files("Photos")
    for file in photo_files:
        url = get_file_url(file)
        if url not in os.listdir("Photos"):
            os.mkdir(f"Photos/{url}")

        os.system(f'move "Photos\\{file}" "Photos\\{url}"')


def main():
    while True:
        # time.sleep(0.5)
        all_files = get_files(None)

        try:
            ignore_files = ["unconfirmed.crdownload", "Unconfirmed.crdownload",
                            "main.py", "README.md", "desktop.ini", "Cleandesk.exe"]
            for ignore_file in ignore_files:
                if ignore_file in all_files:
                    all_files.remove(ignore_files)
        except Exception as e:
            print(e)
            continue

        for file in all_files:
            move_file_to_folder(file)
        classify_photos_in_folder()


if __name__ == "__main__":
    main()
