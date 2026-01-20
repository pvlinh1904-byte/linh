def is_isomorphic(a, b):
    map_ab = {}
    map_ba = {}
    for ca, cb in zip(a, b):
        if ca in map_ab and map_ab[ca] != cb:
            return False
        if cb in map_ba and map_ba[cb] != ca:
            return False
        map_ab[ca] = cb
        map_ba[cb] = ca
    return True
a = input()
b = input()
print(is_isomorphic(a, b))