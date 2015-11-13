t=int(raw_input())
while t!=0:
	s=0
	for i in range(1,t+1):
		s+=(i**2)
	print s
	t=int(raw_input())