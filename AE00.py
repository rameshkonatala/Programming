t=int(raw_input())
l=1
if t==1:
	print 1
elif t==2:
	print 2
else:
	for i in range(t):
		if t<i*i:
			l=i
			break

	c=0		
	for j in range(1,l):
		for k in range(j,t+1):
			if j*k>t:
				break
			else:
				c=c+1

	print c