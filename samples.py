from PIL import Image
import os
from pathlib import Path

import numpy as np

def load_sample(name, rescale=True):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'img' / (name + '.png')
    image = Image.open(path)
    image = image.convert('RGB')
    image = np.asarray(image)

    if rescale:
        image = image.astype(np.float) / 255
    return image

image_names = ['bird', 'ghibli', 'mario', 'scientist', 'tuscany']
all_images = []

for image_name in image_names:
    image = load_sample(image_name, rescale=False)
    all_images.append(image)
    globals()[image_name] = image
