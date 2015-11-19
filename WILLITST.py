#t=int(raw_input())
for i in range(100):
	t=i+1
	s=1
	a=0
	while 2**s<=t:
		if 2**s==t:
			a=1
			break
		else:
			s=s+1
	if a==0:
		print t,"NIE"
	else:
		print t,"TAK"