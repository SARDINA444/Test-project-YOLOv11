import os
import shutil
import random

source_dir = 'noise'

train_dir = 'train'
val_dir = 'val'
test_dir = 'test'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

random.shuffle(all_files)

train_files = all_files[:158]
val_files = all_files[158:178]
test_files = all_files[178:198]


def copy_files(file_list, destination):
    for f in file_list:
        src_path = os.path.join(source_dir, f)
        dst_path = os.path.join(destination, f)
        shutil.copy2(src_path, dst_path)


copy_files(train_files, train_dir)
copy_files(val_files, val_dir)
copy_files(test_files, test_dir)
