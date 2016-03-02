r=int(raw_input())
while r!=0:
	a=[h for h in raw_input()]
	k=1
	x=[]
	while k<=r:
		i=k
		j=(2*r)-k
		while i<=len(a):
			x.append(a[i-1])
			if j<len(a):
				x.append(a[j])
			i=i+(2*r)
			j+=(2*r)
			
		k=k+1
	print "".join(x)
	r=int(raw_input())
		
		