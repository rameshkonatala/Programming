def count(x):
	a=[]
	for i in range(1,x+1):
		a.append(x%i)
	p=max(a)
	t=[]
	for i in range(len(a)):
		if a[i]==p:
			t.append(i+1)
	return max(t)	
			
			
t=int(raw_input())
b=[]
for i in range(t):
	n=int(raw_input())
	b.append(count(n))

	
for i in range(t):
	print b[i]
	
	

		
