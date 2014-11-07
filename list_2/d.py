a = [1,2,2,3]
b = []
def unq(a):
	for k in a:
		if k not in b:
			b.append(k)
	return b




print unq(a)
