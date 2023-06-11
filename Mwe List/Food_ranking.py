import pandas as pd 
import ast
import re 

from num2words import num2words
from collections import defaultdict


def ranking(data, target_column, condition_column, ingredient_rank):

    rank = defaultdict(int)

    for row in data.iterrows():
        name = row[1][target_column]
        ingredients = ast.literal_eval(row[1][condition_column].lower())

        try:
            item = re.sub(r"[^a-zA-Z0-9\s']", ' ', name).lower() 
        except:
            break
            
        cache = []

        for token in item.split():
            if token.isdigit():
                token = num2words(token)

            cache.append(token)

        score = 0

        for ingre in ingredients:
            try:
                score += ingredient_rank[ingre]
            except:
                pass

        rank[' '.join(cache)] = score

        print("count {0} ==> {1}".format(' '.join(cache), score))

    result = sorted(rank.items(), key=lambda x: x[1], reverse=True)

    return result

