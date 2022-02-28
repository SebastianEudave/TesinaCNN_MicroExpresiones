import glob
import os
import pandas as pd
import torch
from PIL import Image
from torch.utils.data import Dataset
import numpy as np

array = []
count = 0
df = pd.DataFrame(columns=["image", "y", "x", "red", "green", "blue"])
count2 = []

for filename in glob.glob('G:/tesina/Licencias/MicroExpressions_Data2/train/disgust/1/EP19_05f'+'/*.jpg'):
    im = Image.open(filename)
    im = im.resize([224, 224])
    count += 1
    colourArray = np.array(im.getdata()).reshape(im.size + (3,))
    indicesArray = np.moveaxis(np.indices(im.size), 0, 2)
    allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))
    df.append(allArray)

print(df)
