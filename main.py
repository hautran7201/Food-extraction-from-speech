import pandas as pd 
import numpy as np

from Ner import *
import os

#food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\food_mwe.npy'
food_path = r'Mwe List\Data\food_mwe.npy'
food_mwe = list(np.load(food_path, allow_pickle=True))

#ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\'ingredient_mwe.npy'
ingredient_path = r'Mwe List\Data\ingredient_mwe.npy'
ingredient_mwe = list(np.load(ingredient_path, allow_pickle=True))

#food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\food_list.npy'
food_path = r'Item List\Data\food_list.npy'
food_list = list(np.load(food_path, allow_pickle=True))

#ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\ingredient_list.npy'
ingredient_path = r'Item List\Data\ingredient_list.npy'
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

