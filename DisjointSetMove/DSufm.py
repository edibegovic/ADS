n, operations = [int(x) for x in input().split()]

primary = [n+int(x) for x in range(0, n)] + [n+int(x) for x in range(0, n)]

size_array = [0 for x in range(0, n)] + [0 for x in range(0, n)]

def find(x):
    if x == primary[x]:
        return x
    else:
        primary[x] = find(primary[x])
        return primary[x]

def query(x, y):
    if find(x) == find(y):
        print("yes")
    else:
        print("no")

def union(x, y):
    x = find(x)
    y = find(y)

    if (x != y):
        if size_array[x] <= size_array[y]:
            primary[x] = y
            size_array[x] += 1
        else:
            primary[y] = x
            size_array[y] += 1

def move(x, y):
    y_root = find(y)
    primary[x] = y_root


# -------------- start --------------

for i in range(operations):
    op, x, y = [x for x in input().split()]
    
    if op == 'q':
        query(int(x), int(y))
    elif op == 'u':
        union(int(x), int(y))
    elif op == 'm':
        move(int(x), int(y))
