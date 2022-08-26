from PIL import Image
import os
from pathlib import Path

import numpy as np

def load_sample(name, rescale=True, crop=True):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'img' / (name + ('_crop' if crop else '') + '.png')
    image = Image.open(path)
    image = np.asarray(image)

    if rescale:
        image = image.astype(np.float) / 255
    return image

sample_names = ['bird']

for sample_name in sample_names:
    globals()[sample_name] = load_sample(sample_name)
