t=int(raw_input())
for i in range(t):
	p,q,x=map(int,raw_input().split())
	if (x%(p+q))==0:
		n=2*(x/(p+q))
	else:
		n=(2*(x/(p+q)))+1
	#print n
	r=(q-p)/(n-5)
	
	#print r
	a=p-(2*r)
	#print a
	alist=[]
	for j in range(n):
		item=str(a+(j*r))
		alist.append(item)
	print n
	print " ".join(alist)
