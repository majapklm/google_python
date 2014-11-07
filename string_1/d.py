a = 'dog'
b = 'dinner'
c = a[:2]
d = a[2:]
e = b[:2]
f = b[2:]
h = []
def fix_word(a,b):
	p = c + f
	q = e + d
	h.append(p)
	h.append(q)
	return " ".join(h)






print fix_word(a,b)
	
