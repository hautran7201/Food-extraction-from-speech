import pandas as pd 
import ast
import re 

from num2words import num2words
from collections import defaultdict


def ranking(data, column, array_item=False):
    raw = data[column].str.strip().to_list()

    rank = defaultdict(int)

    for row in raw:
        if array_item:
            row = ast.literal_eval(row.lower())
        else:
            row = [row]

        for item in row:
            try:
                item = re.sub(r"[^a-zA-Z0-9\s']", ' ', item).lower() 
            except:
                break
            
            cache = []

            for token in item.split():
                if token.isdigit():
                    token = num2words(token)

                cache.append(token)

            rank[' '.join(cache)] += 1 

            print("count {0} ==> {1}".format(' '.join(cache), rank[' '.join(cache)]))

    result = sorted(rank.items(), key=lambda x: x[1], reverse=True)

    return result

