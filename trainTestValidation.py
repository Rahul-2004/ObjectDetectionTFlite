from pathlib import Path
import random
import os
import sys

all_images_path = '/content/images/all'
train_images_path = '/content/images/train'
validation_images_path = '/content/images/validation'
test_images_path = '/content/images/test'

jpeg_files = [path for path in Path(all_images_path).rglob('*.jpeg')]
jpg_files = [path for path in Path(all_images_path).rglob('*.jpg')]
png_files = [path for path in Path(all_images_path).rglob('*.png')]
bmp_files = [path for path in Path(all_images_path).rglob('*.bmp')]

if sys.platform == 'linux':
    JPEG_files = [path for path in Path(all_images_path).rglob('*.JPEG')]
    JPG_files = [path for path in Path(all_images_path).rglob('*.JPG')]
    all_files = jpg_files + JPG_files + png_files + bmp_files + JPEG_files + jpeg_files
else:
    all_files = jpg_files + png_files + bmp_files + jpeg_files

total_files = len(all_files)
print('Total images: %d' % total_files)

train_split = 0.85 # 85% of the files go to train
validation_split = 0.1 # 10% go to validation
test_split = 0.05 # 5% go to test
train_count = int(total_files * train_split)
validation_count = int(total_files * validation_split)
test_count = total_files - train_count - validation_count
print('Images moving to train: %d' % train_count)
print('Images moving to validation: %d' % validation_count)
print('Images moving to test: %d' % test_count)

for _ in range(train_count):
    selected_file = random.choice(all_files)
    file_name = selected_file.name
    file_stem = selected_file.stem
    parent_directory = selected_file.parent
    xml_file_name = file_stem + '.xml'
    os.rename(selected_file, train_images_path + '/' + file_name)
    os.rename(os.path.join(parent_directory, xml_file_name), os.path.join(train_images_path, xml_file_name))
    all_files.remove(selected_file)

for _ in range(validation_count):
    selected_file = random.choice(all_files)
    file_name = selected_file.name
    file_stem = selected_file.stem
    parent_directory = selected_file.parent
    xml_file_name = file_stem + '.xml'
    os.rename(selected_file, validation_images_path + '/' + file_name)
    os.rename(os.path.join(parent_directory, xml_file_name), os.path.join(validation_images_path, xml_file_name))
    all_files.remove(selected_file)

for _ in range(test_count):
    selected_file = random.choice(all_files)
    file_name = selected_file.name
    file_stem = selected_file.stem
    parent_directory = selected_file.parent
    xml_file_name = file_stem + '.xml'
    os.rename(selected_file, test_images_path + '/' + file_name)
    os.rename(os.path.join(parent_directory, xml_file_name), os.path.join(test_images_path, xml_file_name))
    all_files.remove(selected_file)
