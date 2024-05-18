# Задача 4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os
import time


def remove_files_(n):
    """Remove files older than N days."""
    for file in os.listdir('file_deleter_folder'):
        path_file = os.path.join('file_deleter_folder', file)
        # Check if file is exist
        if os.path.isfile(path_file):
            if time.time() - os.stat(path_file).st_mtime > n * 86400:
                os.remove(path_file)
                print(f"{path_file} was removed")


print("Remove files older than N days")
N = int(input("N = "))
remove_files_(n=N)
