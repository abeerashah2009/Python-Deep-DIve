import os
import shutil

directory = os.path.expanduser('~/lab/src')
files = os.listdir(directory)
print("Files in Directory:", sorted(files))

destination = os.path.expanduser('~/lab/dst')
os.makedirs(destination, exist_ok=True)

for file in files:
    source_path = os.path.join(directory, file)
    if os.path.isfile(source_path):
        shutil.copy(source_path, destination)

for file in files:
    source_path = os.path.join(directory, file)
    if os.path.isfile(source_path):
        base, extension = os.path.splitext(file)
        new_name = f"{base}_backup{extension}"
        shutil.copy(source_path, os.path.join(destination, new_name))
