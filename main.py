# ------------------------------------------------------------------------------

# Create mwe
"""import pandas as pd
import numpy as np

from TranscribeText import transcribe_text
from MweCreattion import create_mwe

path = 'Data\RecipeNLG_dataset.csv'

column = ['title']
df = pd.read_csv(path, usecols=column)

mwe = create_mwe(df.sample(frac=0.2), column[0], unique=False)

path = 'Mwe\mwe.npy'
np.save(path, np.array(mwe,  dtype=object))"""

# ------------------------------------------------------------------------------

# Create library
"""import numpy as np 

path = r'ItemList\list.npy'
mwe = np.load(path, allow_pickle=True).tolist()

arr = ['_'.join(i) for i in mwe]

path = r'list.npy'
np.save(path, np.array(arr))"""

# ------------------------------------------------------------------------------

# Test
import pandas as pd 
import numpy as np

from Ner import *
import os

# from TranscribeText import transcribe_text
BASE_DIR = os.getcwd()

#food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\food_mwe.npy'
food_path = os.path.join(BASE_DIR,'Mwe','food_mwe.npy')
food_mwe = list(np.load(food_path, allow_pickle=True))

#ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\'ingredient_mwe.npy'
ingredient_path = os.path.join(BASE_DIR,'Mwe','ingredient_mwe.npy')
ingredient_mwe = list(np.load(ingredient_path, allow_pickle=True))

#food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\food_list.npy'
food_path = os.path.join(BASE_DIR,'ItemList','food_list.npy')
food_list = list(np.load(food_path, allow_pickle=True))

#ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\ingredient_list.npy'
ingredient_path =os.path.join(BASE_DIR,'ItemList','ingredient_list.npy')
ingredient_list = list(np.load(ingredient_path, allow_pickle=True))

mwe = food_mwe + ingredient_mwe
library = food_list + ingredient_list


# Audio data
# audio_path = ''
# data = transcribe_text(audio_path)

# String data
data = 'In a heavy 2-quart saucepan, mix brown sugar, nuts, evaporated milk and butter or margarine.'

result = ingredient_extraction(data, mwe, library)

print('result:', result)

