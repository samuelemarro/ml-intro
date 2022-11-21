import os
from pathlib import Path

import numpy as np

def load_dataset_file(path):
    return np.load(path.as_posix(), allow_pickle=True)
    
def _load_internal_dataset(name):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'data' / name
    return load_dataset_file(path)


def flowers_dataset():
    images = _load_internal_dataset('flowers_images.npy')
    labels = _load_internal_dataset('flowers_labels.npy')
    return images, labels
