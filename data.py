import os
from pathlib import Path

import numpy as np

FLOWERS_URL = 'https://github.com/samuelemarro/ml_intro/releases/download/untagged-1b15fbe0781533e6a82c/flowers.npy'

def flowers_dataset():
    base_path = os.path.abspath(os.path.dirname(__file__))
    path_images = Path(base_path) / 'data' / 'flowers_images.npy'
    images = np.load(path_images.as_posix(), allow_pickle=True)
    path_labels = Path(base_path) / 'data' / 'flowers_labels.npy'
    labels = np.load(path_labels.as_posix(), allow_pickle=True)
    return images, labels
    