from PIL import Image
import random
import os


def random_flip(image, probability=0.5):
    if random.random() < probability:
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image


input_folder = 'bright'
output_folder = 'reflection'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_augmented = random_flip(img, probability=0.7)

        save_path = os.path.join(output_folder, filename)
        img_augmented.save(save_path)

