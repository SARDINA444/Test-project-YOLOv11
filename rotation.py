import os
from PIL import Image
import random


def random_rotate(image, max_angle=30, probability=0.5):
    if random.random() < probability:
        angle = random.uniform(-max_angle, max_angle)
        return image.rotate(angle, resample=Image.BICUBIC, expand=True)
    else:
        return image


input_folder = 'result'

output_folder = 'rotation'

os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):

        img_path = os.path.join(input_folder, filename)

        img = Image.open(img_path)

        img_augmented = random_rotate(img, max_angle=30, probability=0.7)

        save_path = os.path.join(output_folder, filename)
        img_augmented.save(save_path)
