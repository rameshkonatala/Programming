t=int(raw_input())
for i in range(t):
	p,q,x=map(int,raw_input().split())
	if (x%(p+q))!=0:
		a=(p+q)/2
		n=((x/a)-1)/2
		r=(q-a)/(n-2)
		
	else:
		n=(x/(p+q)-1)
		l=n+1
		r=((x/(l))-p)/((2*n)-3)
		a=((x/(n+1)-r)/2)
	
	lis=[]
	if (x%(p+q)!=0):
		print ((2*n)+1)
		for j in range((2*n)+1):
			lis.append(str((a-(n*r))+(j*r)))
	else:
		print ((2*n)+2)
		for j in range((2*n)+2):
			lis.append(str((a-(n*r))+(j*r)))	
	print " ".join(lis)
