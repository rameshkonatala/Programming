def palin(x):
	a=[int(i) for i in str(x)]
	c=0
	for i in range(len(a)/2):
		if a[i]!=a[len(a)-i-1]:
			c=2
			break
	return c	

t=int(raw_input())
for i in range(t):
	p=int(raw_input())+1
	t=1
	while t!=0:
		if palin(p)==0:
			print p
			t=0
		else:
			p=p+1
	