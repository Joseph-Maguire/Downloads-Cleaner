'''
Downloads Cleaner
Joseph Maguire
'''

import os
import collections

# Categorize the file types
EXT_DOCUMENTS = ["txt", "pdf", "xls", "xlsx", "doc", "docx", "html", "csv"]
EXT_IMAGES = ["jpg", "jpeg", "png", "gif", "bmp", "svg"]
EXT_MUSIC = ["mp3", "wav", "wma", "raw", "mdi", "midi"]
EXT_VIDEOS = ["mp4", "avi", "mov", "mpg", "mpeg"]
EXT_APPS = ["exe", "iso", "dmg"]
EXT_COMPRESSED = ["zip", "z", "7z", "rar"]

# Create new directories within the Home directory if they do not exist
HOME_PATH = os.path.expanduser("~")
DESTINATION_DIRECTORIES = ["Documents", "Pictures",
                           "Music", "Videos", "Applications", "Other"]

for direct in DESTINATION_DIRECTORIES:
    dir_path = os.path.join(HOME_PATH, direct)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map the files in the Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(HOME_PATH, "Downloads")
dlFiles_map = collections.defaultdict(list)
dlFiles_list = os.listdir(DOWNLOADS_PATH)

for dlFile_name in dlFiles_list:
    if dlFile_name[0] != ".":
        dlFile_extension = dlFile_name.split(".")[-1]
        dlFiles_map[dlFile_extension].append(dlFile_name)

# Method for moving the files to the correct directories with a check to see if they already exist


def move_file(file_name, dest_folder):
    base_name, ext = os.path.splitext(file_name)
    dest_file_path = os.path.join(dest_folder, file_name)

    # If the file already exists, find the next available version
    counter = 1
    while os.path.exists(dest_file_path):
        new_file_name = f"{base_name}({counter}){ext}"
        dest_file_path = os.path.join(dest_folder, new_file_name)
        counter += 1

    # Now move the file to the destination with the new name
    os.rename(os.path.join(DOWNLOADS_PATH, file_name), dest_file_path)
    print(f"Moved file '{file_name}' to {dest_file_path}.")


# Displat a message if the Downloads folder is empty
if not dlFiles_map:
    print("Can't clean: No files to move. The Downloads folder is empty.")

# Move all the files to the correct directories
for file_extension, file_list in dlFiles_map.items():
    if file_extension in EXT_IMAGES:
        for file in file_list:
            move_file(
                file, os.path.join(HOME_PATH, "Pictures"))
    elif file_extension in EXT_MUSIC:
        for file in file_list:
            move_file(file, os.path.join(HOME_PATH, "Music"))
    elif file_extension in EXT_VIDEOS:
        for file in file_list:
            move_file(file, os.path.join(HOME_PATH, "Videos"))
    elif file_extension in EXT_APPS:
        for file in file_list:
            move_file(
                file, os.path.join(HOME_PATH, "Applications"))
    elif file_extension in EXT_DOCUMENTS or file_extension in EXT_COMPRESSED:
        for file in file_list:
            move_file(
                file, os.path.join(HOME_PATH, "Documents"))
    else:
        for file in file_list:
            move_file(file, os.path.join(HOME_PATH, "Other"))
