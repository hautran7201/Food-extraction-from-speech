import nltk 
import re 
import os

BASE_DIR = os.getcwd()

nltk.download('punkt',download_dir=os.path.join(BASE_DIR,'env'))

def tokenizer(data, mwe=[], lang='english'):
  tokens = []
  tokenizer = nltk.MWETokenizer(mwe)
  data = clean_data(nltk.sent_tokenize(data))
  print(data)
  [tokens.append(tokenizer.tokenize(sentence.split())) for sentence in data] 
  return tokens

def clean_data(data):
  result = []

  for i in data:    
    result.append(re.sub(r"[,.]", " , ", i.lower())) 

  return result