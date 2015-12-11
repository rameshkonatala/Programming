t=raw_input()
a=[]
b=[]
c=[]
j=0
x=-1
p=0
while (str(t) not in b) and t!=1:
	b.append(str(x))
	for k in str(t):
		a.append(k)
	print a
	x=0
	for i in range(len(a)):
		x=x+((int(a[i]))**2)
	t=x
	p=p+1
	
	
else:
	if t==1:
		print p
	else:
		print -1