#Disjoint set excercise one.

a, b = input().split()

disjoint = set(frozenset([c]) for c in range(int(b)))

def find_set(x):
	for i in range(len(disjoint)):
		print(i)
		print(x)
		if x in disjoint:
			return i
	assert False

for i in range(int(b)):
	d, e, f = input().split()
	if d == 'q':
		E = find_set(e)
		F = find_set(f)
		if E == F:
			print('yes')
		else:
			print('no')
	elif d == 'u':
		disjoint.union(e, f)
