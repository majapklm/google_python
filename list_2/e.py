a = [5,4,7,9,1,3,6]
b = [14,2,3,6,9,11,10]
def srt(a):
	s = sorted(a)
	p = sorted(b)
	for k in p:
		s.append(k)
	
	return sorted(s)



print srt(a)
