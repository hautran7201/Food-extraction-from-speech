import pandas as pd
import numpy as np

from MweCreation import *

path = r'Mwe List\Data\ingredient_ranking.npy'
ingredient_rank = np.load(path, allow_pickle=True)

mininum_rank = 1
ir_df = pd.DataFrame(ingredient_rank, columns=['Name', 'count'])
ir_df = ir_df[ir_df['count']>1]

ingredient_mwe = create_mwe(ir_df, 'Name')



path = r'Mwe List\Data\food_ranking.npy'
food_rank = np.load(path, allow_pickle=True)

fd_df = pd.DataFrame(ingredient_rank, columns=['Name', 'count'])

food_mwe = create_mwe(fd_df, 'Name')

mwe = ingredient_mwe + food_mwe 


path = 'Mwe List\Data\mwe.npy'
np.save(path, np.array(mwe,  dtype=object))