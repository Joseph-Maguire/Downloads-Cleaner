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

# Move all the files to correct directories

for file_extension, file_list in dlFiles_map.items():

    if file_extension in EXT_IMAGES:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Pictures", file))

    elif file_extension in EXT_MUSIC:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Music", file))

    elif file_extension in EXT_VIDEOS:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Videos", file))

    elif file_extension in EXT_APPS:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Applications", file))

    elif file_extension in EXT_DOCUMENTS or file_extension in EXT_COMPRESSED:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Documents", file))

    else:
        for file in file_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file),
                      os.path.join(HOME_PATH, "Other", file))
