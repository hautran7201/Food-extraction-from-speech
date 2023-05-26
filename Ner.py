import spacy
import numpy as np 
import sys

from Utils import *
spa = spacy.load("en_core_web_sm")

def pos_tagger_spacy(data, mwe=[]): 
  tokenized_text = [" ".join(i) for i in tokenizer(data, mwe)]
  spacy_token = list(spa.pipe(tokenized_text))
  return spacy_token

def entity_tagger_spacy(data, library, condition=['PROPN', 'NOUN']):
  entity_tokens = []
  for r in data:
    for c in r:
      word, tag = c.text, c.pos_
      token_tag = []
      
      for token in spa(word.replace('_', ' ')):
        token_tag.append([token.text, token.pos_, token.is_stop])

      if (word in library) and sum([(i in np.array(token_tag)[:, 1]) for i in condition]) > 0:
        for index, token in enumerate([i[0] for i in token_tag if i[2]==False]):
          if index==0:
            entity_tokens.append(token+' '+'B-INGREDIENT'+' '+tag)
          else:
            entity_tokens.append(token+' '+'I-INGREDIENT'+' '+tag)
      else: 
        entity_tokens.append(word+' '+'O'+' '+tag)
  
  return entity_tokens

def bio_extraction(entity_list):
  result = []
  cache = []
  
  for i in entity_list:
    token = i.split(' ')     
    if token[1] != 'O':
      cache.append(token)

  index = np.where(np.array(cache)[:, 1] == 'B-INGREDIENT')[0].tolist()
  index = list(index) + [len(cache)]  

  for i in range(0, len(index)-1):
    result.append(cache[index[i]:index[i+1]])
    
  return result

def ingredient_extraction(data, mwe, library, condition=['NOUN', 'PROPN']):  

  docs = pos_tagger_spacy(data, mwe)

  entity = entity_tagger_spacy(docs, library, condition)

  bio = bio_extraction(entity)

  result = []
  for item in bio:
    cache = []
    for token in item:
        cache.append(token[0])
    result.append(" ".join(cache))

  return result


if __name__ == '__main__':

  food_path = r'C:\Users\soaic\Desktop\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\food_mwe.npy'
  #food_path = r'Mwe List\Data\food_mwe.npy'
  food_mwe = list(np.load(food_path, allow_pickle=True))

  ingredient_path = r'C:\Users\soaic\Desktop\EXE\Vetula app\Ingredient extraction from speech - Copy\Mwe\ingredient_mwe.npy'
  #ingredient_path = r'Mwe List\Data\ingredient_mwe.npy'
  ingredient_mwe = list(np.load(ingredient_path, allow_pickle=True))

  food_path = r'C:\Users\soaic\Desktop\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\food_list.npy'
  #food_path = r'Item List\Data\food_list.npy'
  food_list = list(np.load(food_path, allow_pickle=True))

  ingredient_path = r'C:\Users\soaic\Desktop\EXE\Vetula app\Ingredient extraction from speech - Copy\ItemList\ingredient_list.npy'
  #ingredient_path = r'Item List\Data\ingredient_list.npy'
  ingredient_list = list(np.load(ingredient_path, allow_pickle=True))

  # Create mwe and library variable
  mwe = food_mwe + ingredient_mwe
  library = food_list + ingredient_list

  # Input paramaters from command line
  path = sys.argv[1] if len(sys.argv) > 1 else None
  condition = sys.argv[2] if len(sys.argv) > 2 else ['NOUN', 'PROPN']

  # Load data from file
  file = open(path, 'r')

  # Read file
  data = file.read()

  # Close file
  file.close()

  print('\nRaw text:')
  print(data)

  print('\nEntity extraction:')
  print(ingredient_extraction(data, mwe, library, condition))
