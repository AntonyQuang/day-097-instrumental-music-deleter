import os
import send2trash


# There is no special type for raw strings; it is just a string,
# which is equivalent to a regular string with backslashes represented by \\ .
# In a normal string, an escape sequence is considered to be one character,
# but in a raw string, backslashes are also counted as characters.

# The r converts a normal string into a raw string.
music_path = r"C:\Users\NAME\Music"
deleted_songs_list = []
# os.listdir(folder + "\\" + entry)


def open_folder(folder):
    entries = os.listdir(folder)
    files_and_folders = [get_path(folder, file_or_folder_name) for file_or_folder_name in entries]
    return files_and_folders


def get_path(parent, item):
    path = parent + "\\" + item
    return path


def instrumental_check(file_path):
    if "instrumental" in file_path.lower() or "off-vocal" in file_path.lower() or "karaoke" in file_path.lower():
        # send to recycling bin instead of permanently deleting file
        send2trash.send2trash(file_path)
        return file_path


def app(parent_path):
    folder_contents = open_folder(parent_path)
    for path in folder_contents:
        if os.path.isfile(path):
            if instrumental_check(path):
                deleted_songs_list.append(path)
        else:
            # recursion
            app(path)


run = app(music_path)
print(*deleted_songs_list, sep='\n')