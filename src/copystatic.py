from os import path, mkdir, listdir, getcwd
from shutil import copy, rmtree


def copy_static(source_dir_path, destination_dir_path):
    # first delete contents of destination folder
    # check if directory exists, remove it and its contents
    if not path.exists(destination_dir_path):
        # create new directory in root called public
        mkdir(destination_dir_path)
        # recursively
        # list contents of static
        # base case: single file (or no files) copy all [if is file]
        # if directory, check directory contents and copy if file
    contents = listdir(source_dir_path)
    for file in contents:
        src_path = path.join(source_dir_path, file)
        dest_path = path.join(destination_dir_path, file)

        if path.isfile(src_path):
            print('Copying ', src_path)
            copy(src_path, dest_path)
        else:
            copy_static(src_path, dest_path)
