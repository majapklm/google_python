a = 'maja'
b = 'hinmal'
def front_back(a,b):
	if (len(a)%2 == 0) and (len(b)%2 == 0):
		p = a[:len(a)/2] + b[:len(b)/2]
		q = a[len(a)/2:] + b[len(b)/2:]
		return p + q
	else:
		r =  a[:len(a)/2+1] + b[:len(b)/2+1]
		s =  a[len(a)/2:] + b[len(b)/2:]	
		return r + s







print front_back(a,b)
