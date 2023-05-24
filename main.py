"""import pandas as pd
import numpy as np

from TranscribeText import transcribe_text
from MweCreattion import create_mwe

path = 'D:\EXE\Vetula app\Ingredient extraction from speech\Data\RecipeNLG_dataset.csv'

column = ['title']
df = pd.read_csv(path, usecols=column)

mwe = create_mwe(df.sample(frac=0.2), column[0], unique=False)

path = 'D:\EXE\Vetula app\Ingredient extraction from speech\MWE\mwe.npy'
np.save(path, np.array(mwe,  dtype=object))"""

# ------------------------------------------------------------------------------

"""import numpy as np 

path = r'D:\EXE\Vetula app\Ingredient extraction from speech\MWE\ingredient_mwe.npy'
mwe = np.load(path, allow_pickle=True).tolist()

arr = ['_'.join(i) for i in mwe]

path = r'D:\EXE\Vetula app\Ingredient extraction from speech\ItemList\list.npy'
np.save(path, np.array(arr))"""

# ------------------------------------------------------------------------------

import pandas as pd 
import numpy as np

from Ner import *

data = 'In a heavy 2-quart saucepan, mix brown sugar, nuts, evaporated milk and butter or margarine.'

food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech\MWE\food_mwe.npy'
food_mwe = list(np.load(food_path, allow_pickle=True))

ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech\MWE\ingredient_mwe.npy'
ingredient_mwe = list(np.load(ingredient_path, allow_pickle=True))

food_path = r'D:\EXE\Vetula app\Ingredient extraction from speech\ItemList\food_list.npy'
food_list = list(np.load(food_path, allow_pickle=True))

ingredient_path = r'D:\EXE\Vetula app\Ingredient extraction from speech\ItemList\ingredient_list.npy'
ingredient_list = list(np.load(ingredient_path, allow_pickle=True))

mwe = food_mwe + ingredient_mwe
library = food_list + ingredient_list
result = ingredient_extraction(data, mwe, library)

print('result:', result)

