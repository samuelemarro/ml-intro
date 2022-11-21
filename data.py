import os
from pathlib import Path

import numpy as np

def _load_dataset(name):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'data' / name
    return np.load(path.as_posix(), allow_pickle=True)


def flowers_dataset():
    images = _load_dataset('flowers_images.npy')
    labels = _load_dataset('flowers_labels.npy')
    return images, labels

def papaya_pumpkin_dataset():
    images = _load_dataset('papaya_pumpkin_images.npy')
    labels = _load_dataset('papaya_pumpkin_labels.npy')
    return images, labels
