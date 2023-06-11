import re
import ast
from collections import defaultdict
from num2words import num2words


def create_mwe(data, column):
    raw = data[column].str.strip().to_list()

    mwe = []

    count = 0
    for item in raw:
        try:
            item = re.sub(r"[^a-zA-Z0-9\s']", " ", item).lower()
        except:
            break

        cache = []

        for token in item.split():
            if token.isdigit():
                token = num2words(token)

            cache.append(token)

        mwe.append(cache)
        count += 1
        print("count {0} ==> {1}".format(count, cache))

    return mwe


def food_ranking(data, target_column, condition_column, ingredient_rank):

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


def ingredient_ranking(data, column, array_item=False):
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