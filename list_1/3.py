a = [(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
def myfn(a):
	return a[-1] 
def srt (a):
	return sorted(a,key = myfn)




print srt(a)

