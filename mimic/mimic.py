a='alice.txt'
def mimic_dict(a):
	mimic_dict={}
	f=open(a,'r')
	text=f.read()
	f.close()
	words=text.split()
	prev=''
	for word in words:
		if not prev in mimic_dict:
			mimic_dict[prev]=[word]
		else:
			mimic_dict[prev].append(word)
		prev=word
	print mimic_dict

mimic_dict('alice.txt')
