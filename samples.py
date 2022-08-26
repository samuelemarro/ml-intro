from PIL import Image
import os
from pathlib import Path

import numpy as np

def load_sample(name, rescale=False, drop_alpha=True):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'img' / (name + '.png')
    image = Image.open(path)
    if drop_alpha:
        image = image.convert('RGB')
    image = np.asarray(image)

    if rescale:
        image = image.astype(np.float) / 255
    return image

image_names = ['bird', 'ghibli', 'mario', 'scientist', 'tuscany']
standard_images = []

for image_name in image_names:
    image = load_sample(image_name)
    standard_images.append(image)
    globals()[image_name] = image

class Special:
    def __init__(self):
        self.sunglasses_noalpha = load_sample('sunglasses_alpha', drop_alpha=False)
        self.sunglasses_alpha = load_sample('sunglasses_noalpha')

special = Special()