import nltk 
import re 
import os
import gdown
import sys

def read_file(path):
  file = open(path, 'r')

  # Read file
  content = file.read()

  # Close file
  file.close()

  return content

def write_file(path, data):
  file = open(path, 'w')

  # Write file
  file.write(data)

  # Close file
  file.close()

def download_data():
  source = {
    'ItemList': read_file('Item List\Data\Source.txt'),
    'MweList': read_file('Mwe List\Data\Source.txt')
  }

  # Download ItemList
  gdown.download_folder(source['ItemList'], output='Item List\Data')

  # Download MweList
  gdown.download_folder(source['MweList'], output='Mwe List\Data')


def tokenizer(data, mwe=[], lang='english'):
  tokens = []
  tokenizer = nltk.MWETokenizer(mwe)
  data = clean_data(nltk.sent_tokenize(data))
  [tokens.append(tokenizer.tokenize(sentence.split())) for sentence in data] 
  return tokens

def clean_data(data):
  result = []

  for i in data:    
    result.append(re.sub(r"[,.]", " , ", i.lower())) 

  return result

if __name__ == '__main__':
  globals()[sys.argv[1]]()