def FindSub(large, small):
    if len(large) < len(small):
        return -1
    if len(small) == 0:
        return 0
    first = small[0]
    index = 0
    while index <= len(large) - len(small):
        if large[index] == first:
            if large[index: index + len(small)] == small:
                return index
        index  = index + 1
    return -1
print FindSub( 'spar', 'sh')
