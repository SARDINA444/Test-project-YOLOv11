from PIL import Image, ImageEnhance
import random
import os


def random_brightness_contrast(image, brightness_range=(0.7, 1.3), contrast_range=(0.7, 1.3), probability=0.5):
    if random.random() < probability:

        brightness_factor = random.uniform(*brightness_range)
        enhancer_brightness = ImageEnhance.Brightness(image)
        image = enhancer_brightness.enhance(brightness_factor)

        contrast_factor = random.uniform(*contrast_range)
        enhancer_contrast = ImageEnhance.Contrast(image)
        image = enhancer_contrast.enhance(contrast_factor)

    return image


input_folder = 'scale'
output_folder = 'bright'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_augmented = random_brightness_contrast(
            img,
            brightness_range=(0.7, 1.3),
            contrast_range=(0.7, 1.3),
            probability=0.7
        )

        save_path = os.path.join(output_folder, filename)
        img_augmented.save(save_path)
