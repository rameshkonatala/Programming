def prime(x):
	t=0
	if x==1 :
		t=1
	elif x==2 or x==3:
		t=0
	else:
		for i in range(2,(x/2)+1):
			if x%i==0:
				t=1
				break
	if t==1:
		return 1
	else:
		return 0
	
def remove(z,t):
	for x in range(1,(len(z)+1)):
		if (x*t) in z:
			z.remove(x*t)
	return z
	
#z=[3,5,7,9]
#g=3
#print remove(z,g)

t=int(raw_input())
for i in range(t):
	a,b=map(int,raw_input().split())
	x=[int(i) for i in range(a,b+1)]
	if x[0]==1:
		x=x[1:]
		
	t=len(x)
	
	while t>0:
		m=prime (x[0])
		if m==0:
			print x[0]
		x=remove(x,x[0])
		t=len(x)
	print " "
	
	