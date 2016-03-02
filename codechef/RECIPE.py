def fact(x):
	a=[]
	for i in range(x+1,1,-1):
		if x%i==0:
			a.append(i)
	return a
	
	
def listratio(k,p):
	q=tuple(p)
	for i in range(len(p)):
		t=0
		if int(p[i])%k!=0:
			t=1
			break
		else:
			p[i]=int(p[i])/k
			
		
	if t==0:
		return p
	else:
		return list(q)
	


t=int(raw_input())
for i in range(t):
	b=raw_input().split()
	b.remove(b[0]);
	a=min(int(s) for s in b)
	
	for j in fact(a):
		b=listratio(j,b)
		
	print " ".join(str(x) for x in b)