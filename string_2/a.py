s = 'fooding'
def verbing(s):
	if len(s)>3:
	
		if s[-3:] == 'ing':
			return s.replace(s[-3:],'ly')
		else:
			return s + 'ing'

	
	else:
		return s
	





print verbing(s)
