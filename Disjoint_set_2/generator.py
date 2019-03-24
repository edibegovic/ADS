import sys, random
n = int(sys.argv[1])
print(n ,n)

for i in range(n):
    s = random.choice(range(n))
    t = random.choice(range(n))
    if random.choice(range(6)) > 0:
        print('u', s, t)
    else:
        print('q', s, t)
    
