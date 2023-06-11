import pandas as pd
import numpy as np
from MweCreation import *

# Create ingredient ranking list
path = r'Data\Source\RecipeNLG_dataset.csv'
column = ['NER']
df = pd.read_csv(path, usecols=column)

rank = ingredient_ranking(df, column[0], array_item=True)

path = r'Mwe List\Data\ingredient_ranking.npy'
np.save(path, np.array(rank,  dtype=object))



# Create food ranking list
path = r'Data\Source\RecipeNLG_dataset.csv'
column = ['title', 'NER']
df = pd.read_csv(path, usecols=column)

path = r'Mwe List\Data\food_ranking.npy'
ingredient_rank = dict(np.load(path, allow_pickle=True))

rank = food_ranking(df, 'title', 'NER', ingredient_rank)

path = r'Mwe List\Data\food_ranking.npy'
np.save(path, np.array(rank,  dtype=object))