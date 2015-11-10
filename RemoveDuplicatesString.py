def Duplicates(string):
    d1 = {}
    for items in string:
        d1[items] = d1.get(items, 0) + 1

    new_string = ''
    for items in string:
        if items in d1:
            new_string += items
            del d1[items]
    return new_string
