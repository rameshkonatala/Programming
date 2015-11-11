def fact(x):
	a=[]
	for i in range(x+1,2,-1):
		if x%i==0:
			a.append(i)
	return a
	
def listratio(j,b):
	for i in range(len(b)):
		t=0
		if int(b[i])%j!=0:
			break
		else:
			b[i]=int(b[i])/j
	
	return b
	


t=int(raw_input())
for i in range(t):
	b=raw_input().split()
	b.remove(b[0]);
	a=int(min(b))
	for j in fact(a):
		b=listratio(j,b)
	print " ".join(str(x) for x in b)