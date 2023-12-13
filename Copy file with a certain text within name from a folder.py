import os
import shutil

def search_and_copy(src, dst, target):
    for dirpath, dirnames, filenames in os.walk(src):
        for filename in filenames:
            if target in filename:
                source_file_path = os.path.join(dirpath, filename)
                destination_file_path = os.path.join(dst, filename)
                shutil.copy2(source_file_path, destination_file_path)
                print(f'Copied file {filename} to {dst}')

# Set the source folder and destination folder
src_folder = 'Accounting'
dst_folder = 'destination_folder'

# Set the target text
target_text = 'Krista'

# Create the destination directory if it doesn't exist
os.makedirs(dst_folder, exist_ok=True)

search_and_copy(src_folder, dst_folder, target_text)
