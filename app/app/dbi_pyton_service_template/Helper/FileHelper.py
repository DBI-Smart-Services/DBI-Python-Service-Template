import os
import shutil


def create_tmp_folder():
    """
    Creates a tmp folder in the source directory if it does not exist
    """
    if not os.path.exists("tmp"):
        os.mkdir("tmp")


def clear_tmp_folder():
    """
    Clears the tmp folder
    """
    if os.path.exists("tmp"):
        shutil.rmtree("tmp")
    create_tmp_folder()
