def candy(b,x):
	if (x%len(b)!=0):
		return -1
		
	
	else:
		t=0
		for i in range(len(b)):
			if b[i]>(x/len(b)):
				t=t+(b[i]-(x/len(b)))
		return t



t=int(raw_input())
while t!=-1:
	s=0
	a=[]
	for i in range(t):
		a.append(int(raw_input()))
		s=s+a[i]
	print candy(a,s)
	t=int(raw_input())