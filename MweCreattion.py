import re
import ast

from num2words import num2words
def create_mwe(data, column, array_item=False, unique=True):
    raw = data[column].str.strip().to_list()

    mwe = []

    count = 0
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

            if unique:
                if cache not in mwe:
                    mwe.append(cache)
                    count += 1
                    print("count {0} ==> {1}".format(count, cache))
            else:
                mwe.append(cache)
                count += 1
                print("count {0} ==> {1}".format(count, cache))

    return mwe
