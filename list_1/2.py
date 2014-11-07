a = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] 
def myfn(a):
	return (a[0]=='x')
def srt (a):
	return sorted(a,key = myfn)[::-1]
print srt(a)


