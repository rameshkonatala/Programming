p=int(raw_input())
while p!=0: 
	a=map(int,raw_input().split())
	t=0
	j=0
	k=1
	top=p+1
	while j<len(a) and t==0:
		if k!=a[j] and top>a[j]:
			top=a[j]
			
		elif len(c)>0 and k==c(len(c)-1):
			c.append(a[j])
			if len(c)>1 and c[len(c)-2]<c[len(c)-1]:
				t=1
		else:
			k=k+1
		
		j=j+1

	if t==0:
		print "Yes"
	else:
		print "No"
	p=int(raw_input())