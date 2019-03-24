#quick union

def root(array, p):
    while array[p] != p:
        p = array[p]
    return p

def connected(array, p, q):
    return find(array, p) == find(array, q)

def union(array, p, q):
    if connected(array, p, q):
        return
    else:
        array[root(array, p)] == root(array, q)
        return

def move():