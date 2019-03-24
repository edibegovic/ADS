#Disjoint set excercise two.
from algs4.fundamentals.uf import WeightedQuickUnionUF
a, b = input().split()

disjoint = WeightedQuickUnionUF(int(a))

for i in range(int(b)):
    d, e, f = input().split()
    if d == 'q':
        if disjoint.connected(int(e), int(f)) == True:
            print('yes')
        else:
            print('no')
    elif d == 'u':
        disjoint.union(int(e), int(f))
