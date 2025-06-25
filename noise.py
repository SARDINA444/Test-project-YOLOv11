import numpy as np
from PIL import Image
import random
import os


def add_random_noise(image, noise_level=0.05, probability=0.5):
    if random.random() < probability:
        img_array = np.array(image).astype(np.float32) / 255.0

        noise = np.random.randn(*img_array.shape) * noise_level

        noisy_img = img_array + noise
        noisy_img = np.clip(noisy_img, 0, 1)

        noisy_img = (noisy_img * 255).astype(np.uint8)
        return Image.fromarray(noisy_img)
    else:
        return image


input_folder = 'reflection'
output_folder = 'noise'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        img_noisy = add_random_noise(img, noise_level=0.05, probability=0.7)

        save_path = os.path.join(output_folder, filename)
        img_noisy.save(save_path)
