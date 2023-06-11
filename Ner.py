import spacy
import numpy as np 
import time

from Utils import *
spa = spacy.load("en_core_web_sm")

def pos_tagger_spacy(data, mwe=[]): 
  tokenized_text = [" ".join(i) for i in tokenizer(data, mwe)]
  spacy_token = list(spa.pipe(tokenized_text))
  
  return spacy_token

def entity_tagger_spacy(data, mwe, condition=['PROPN', 'NOUN']):
  entity_tokens = []

  for r in data:
    for c in r:
      word, tag = c.text, c.pos_
      token_tag = []

      for token in spa(word.replace('_', ' ')):
        token_tag.append([token.text, token.pos_, token.is_stop])

      if (word.split('_') in mwe) and sum([(i in np.array(token_tag)[:, 1]) for i in condition]) > 0:
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

def ingredient_extraction(data, mwe, condition=['NOUN', 'PROPN']):  

  docs = pos_tagger_spacy(data, mwe)

  entity = entity_tagger_spacy(docs, mwe, condition)

  bio = bio_extraction(entity)

  result = []
  for item in bio:
    cache = []
    for token in item:
        cache.append(token[0])
    result.append(" ".join(cache))

  return result


if __name__ == '__main__':

  path = r'Mwe List\Data\mwe.npy'
  #food_path = r'Mwe List\Data\food_mwe.npy'
  mwe = list(np.load(path, allow_pickle=True))

  # Input paramaters from command line
  path = sys.argv[1] if len(sys.argv) > 1 else None
  condition = sys.argv[2] if len(sys.argv) > 2 else ['NOUN', 'PROPN']
  data = read_file(path)

  # Extract entity from text
  result = ingredient_extraction(data, mwe, condition)

  # Save entity list to file
  file_name = os.path.basename(path)
  name = os.path.splitext(file_name)[0]

  path = f'Data\Entity\{name}.txt'

  file = open(path,'w')
  for item in result:
    file.write(item+"\n")
  file.close()

  print(result)
