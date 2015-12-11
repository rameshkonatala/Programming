def rev(alist):
	b=[]
	for i in range(len(alist)):
		b.append(alist[len(alist)-1-i])
	return b
	
t=int(raw_input())
for i in range(t):
	p=raw_input()
	a=[ch for ch in p]
	
	n=len(a)
	if len(a)==1:
		if int(a[0])==9:
			print 11
		else:
			print int(a[0])+1
	else:
		
		if len(a)%2==0:
			b=int("".join(a[:(n/2)]))+1
			m=[]
			for k in str(b):
				m.append(k)
			#print m
			c=list(rev(m))
			print ("".join(m+c))
		else:
			b=int("".join(a[:((n/2)+1)]))+1
			m=[]
			for k in str(b):
				m.append(k)
			#print m
			c=list(rev(m))
			
			print ("".join(m+c[1:]))
	