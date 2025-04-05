import os


def create_temp_folder():

    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, "temp")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path
