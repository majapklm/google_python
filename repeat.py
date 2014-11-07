def repeat(s,exclaim):
	print """returns the string s repeated 3 times..
if exclaim is true,add exclamation marks..."""

	result=s*3
	if exclaim:
		result=result +	'!!!'
	return result



print repeat('python',1)
