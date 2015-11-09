def ambiguous(x):
	p=[]
	t=0
	for i in range(len(x)):
		p.append(str(x.index(str(i+1))+1))
		
		if p[i]!=x[i]:
			t=1
			break
	
	if t==0:
		return 1	
	else:
		return 2

		
p=int(raw_input())
b=[]
while p!=0:
	a=raw_input().split()
	
	q= ambiguous(a)
	b.append(q)
	p=int(raw_input())

	
for i in range(len(b)):
	if b[i]==1:
		print "ambiguous"	
	else:
		print "not ambiguous"
