from PIL import Image
import random
import os


def random_scale_shift(image, scale_range=(0.8, 1.2), shift_range=0.2, probability=0.5):
    if random.random() < probability:
        width, height = image.size

        scale_factor = random.uniform(*scale_range)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        image = image.resize((new_width, new_height), resample=Image.BICUBIC)

        max_dx = shift_range * width
        max_dy = shift_range * height
        dx = random.uniform(-max_dx, max_dx)
        dy = random.uniform(-max_dy, max_dy)

        shifted_image = Image.new("RGB", (width, height))

        left = int(dx + (width - new_width) / 2)
        top = int(dy + (height - new_height) / 2)

        shifted_image.paste(image, (left, top))

        return shifted_image
    else:
        return image


input_folder = 'rotation'
output_folder = 'scale'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_augmented = random_scale_shift(img, scale_range=(0.8, 1.2), shift_range=0.2, probability=0.7)

        save_path = os.path.join(output_folder, filename)
        img_augmented.save(save_path)
