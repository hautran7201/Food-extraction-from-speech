import numpy as np 

path = 'Mwe List\Data\[Filename].npy'
mwe = np.load(path, allow_pickle=True).tolist()

arr = ['_'.join(i) for i in mwe]

path = 'Item List\Data\[filename].npy'
np.save(path, np.array(arr))