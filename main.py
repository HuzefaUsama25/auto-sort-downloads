import os


def get_files():
    all_items = os.listdir()
    files = [i for i in all_items if "." in i]
    return files


def get_file_extension(file):
    extension = file.split(".")[-1]
    return extension


def get_file_url(file):
    url = os.popen(f"powershell Get-Content {file} -Stream Zone.Identifier").read(
    ).split("\n")[-2].replace("HostUrl=", "")
    domain = url.split(".")[1]
    return domain


def move_file_to_folder(file):
    file_folder_map = {
        ".exe": "Applications & Games",
        ".png": "Photos",
        ".jfif": "Photos",
        ".jpg": "Photos",
        ".jpeg": "Photos",
        ".mp3": "Music"
    }

    extension = get_file_extension(file)

    folder_to_put_in = file_folder_map.get(extension)

    if folder_to_put_in not in os.listdir():
        os.mkdir(folder_to_put_in)

    os.system(f"move {file} {folder_to_put_in}")


def classify_photos_in_folder():
    # calssify photos according to source!
    photo_files = os.listdir("Photos")

    for file in photo_files:
        url = get_file_url(file)

        if url not in os.listdir("Photos"):
            os.mkdir("Photos/{url}")

        os.system("move '{file}' 'Photo/{url}'")


def main():
    while True:
        all_files = get_files()


if __name__ == "__main__":
    main()
