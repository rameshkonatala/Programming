t=int(raw_input())
a=[]
b=[]
c=[]
p=0
while t not in c or t!=1:
	a.append(i for i in str(t))
	x=0
	print a
	for i in range(len(a)):
		x=x+((int(a[i]))**2)
	c=b
	b.append(str(x))
	t=str(x)
	p=p+1
	
else:
	if t==1:
		print p
	else:
		print -1
	