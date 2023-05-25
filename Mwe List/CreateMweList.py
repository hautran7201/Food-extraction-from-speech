import pandas as pd
import numpy as np

from TranscribeText import transcribe_text
from MweCreation import create_mwe

path = 'Data\RecipeNLG_dataset.csv'

column = ['title']
df = pd.read_csv(path, usecols=column)

mwe = create_mwe(df.sample(frac=0.2), column[0], unique=False)

path = 'Mwe List\Data\[Filename].npy'
np.save(path, np.array(mwe,  dtype=object))