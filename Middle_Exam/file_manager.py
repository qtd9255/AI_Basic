import os
import shutil

def list_files(folder):
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def create_folder(base, name):
    path = os.path.join(base, name)
    os.makedirs(path, exist_ok=True)
    return path

def move_file(src_folder, dst_folder, filename, new_name=None):
    src = os.path.join(src_folder, filename)
    dst_name = new_name if new_name else filename
    dst = os.path.join(dst_folder, dst_name)
    shutil.move(src, dst)
