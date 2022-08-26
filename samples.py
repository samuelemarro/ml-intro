from PIL import Image
import os
from pathlib import Path

import numpy as np

def load_sample(name, rescale=True):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'img' / (name + '.png')
    image = Image.open(path)
    image = np.asarray(image)

    if rescale:
        image = image.astype(np.float) / 255
    return image

sample_names = ['bird', 'ghibly', 'mario', 'scientist', 'tuscany']
all_images = []

for sample_name in sample_names:
    image = load_sample(sample_name)
    all_images.append(image)
    globals()[sample_name] = image
