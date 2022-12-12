import os
from pathlib import Path
import json

import numpy as np
import pandas as pd

def load_dataset_file(path):
    if isinstance(path, Path):
        path = path.as_posix()
    return np.load(path, allow_pickle=True)
    
def _load_internal_dataset(name):
    base_path = os.path.abspath(os.path.dirname(__file__))
    path = Path(base_path) / 'data' / name
    return load_dataset_file(path)


def flowers_dataset():
    images = _load_internal_dataset('flowers_images.npy')
    labels = _load_internal_dataset('flowers_labels.npy')
    return images, labels

def ecg_dataset():
    inputs = _load_internal_dataset('ecg_values.npy')
    labels = _load_internal_dataset('ecg_labels.npy')
    return inputs, labels

def meteo_dataset():
    return _load_internal_dataset('meteo.npy')

def sp250_dataset():
    with open('data/sp250_info.json') as f:
        data = json.load(f)
    return _load_internal_dataset('sp250_values.npy'), np.array(data['category']), data['names'], data['category_names']

def headlines_dataset():
    data = pd.read_csv('data/headlines.csv')

    return list(data['headlines']), list(data['complete_text'])