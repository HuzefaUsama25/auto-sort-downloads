import os
import time

# get all the files present in your directory


def get_files(directory):
    all_items = os.popen(f'dir /b "{directory}"').read().split('\n')
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

        if "Error" in raw_url:
            return "Other"
        else:
            # clean the zone identifier to get url and clean it.
            url = raw_url.split("\n")[-2].replace("HostUrl=", "")
            # get the domain name of the url. such as: google, pinterest, etc.
            domain = url.split(".")[1]
            return domain
    except Exception as e:
        print(e)
        return "Other"


def move_file_to_folder(file):
    # file extensions to associate with folders
    file_folder_map = {
        "exe": "Executables",
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
        "webp": "Photos",
        "mp3": "Music",
        "wav": "Music",
        "wma": "Music",
        "aac": "Music",
        "ogg": "Music",
        "m4a": "Music",
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
        "7z": "Compressed-Files",
        "zip": "Compressed-Files",
        "rar": "Compressed-Files",

    }

    extension = get_file_extension(file)
    folder_to_put_in = file_folder_map.get(extension)

    print(f"{file} --> {extension} --> {folder_to_put_in}\n")

    if folder_to_put_in == None:
        folder_to_put_in = "Unidentified"

    if folder_to_put_in not in os.listdir():
        os.mkdir(folder_to_put_in)

    os.system(f'move "{file}" "{folder_to_put_in}"')


def classify_files_in_folder():
    # classify files in folder according to source url.
    folders_to_work_in = ["Photos", "Executables",
                          "Setups", "Music", "Videos", "Documents", "Compressed-Files"]
    for folder in folders_to_work_in:
        if folder in os.listdir(None):
            files = get_files(folder)
            for file in files:
                url = get_file_url(file)
                if url is not None:
                    if url not in os.listdir(folder):
                        os.mkdir(f"{folder}/{url}")

                    os.system(f'move "{folder}\\{file}" "{folder}\\{url}"')


def main():
    while True:
        # time.sleep(0.5)
        all_files = get_files("")
        try:
            ignore_files = ["unconfirmed.crdownload", "Unconfirmed.crdownload",
                            "main.py", "README.md", "Cleandesk.exe"]
            for ignore_file in ignore_files:
                if ignore_file in all_files:
                    all_files.remove(ignore_file)
        except Exception as e:
            print(e)
            continue

        for file in all_files:
            move_file_to_folder(file)
        classify_files_in_folder()


if __name__ == "__main__":
    main()
