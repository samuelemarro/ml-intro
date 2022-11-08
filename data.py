import os
from pathlib import Path

import numpy as np

FLOWERS_URL = 'https://github.com/samuelemarro/ml_intro/releases/download/untagged-1b15fbe0781533e6a82c/flowers.npy'

def flowers_dataset():
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'data' / 'flowers.npy'
    images, labels = np.load(path.as_posix(), allow_pickle=True)
    return images, labels
    