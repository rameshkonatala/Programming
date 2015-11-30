def palin(a):
	
	if len(a)<=1:
		return True
		
	elif a[0]!=a[len(a)-1]:
		return False
		
	else:
		a.pop()
		a.pop(0)
		return palin(a) 
		
t=int(raw_input())
for i in range(t):
	p=int(raw_input())+1
	t=1
	while t!=0:
		if palin([j for j in str(p)]):
			print p
			t=0
		else:
			
			p=p+1