t=int(raw_input())
for i in range(t):	
	a=[i for i in raw_input()]
	l=len(a)
	i=0
	while l!=1:
		if a[i]!="(" and a[i+1]!="(" and a[i+2]!="(":
			p=a[i+1]
			q=a[i+2]
			a[i]=a[i]+q+p
			
			del a[i-1]
			del a[i]
			del a[i]
			del a[i]
			
			
			i=0
			
		else:
			i=i+1
			
		l=len(a)
		
	print a[0]	