t=int(raw_input())
for i in range(t):
	raw_input()
	b=int(raw_input())
	p=[]
	
	for j in range(b):
		p.append(int(raw_input()))
	
	c=sorted(p)
	print c
	m=0
	w=1
	k=b-1
	while w>0:
		l=p.index(c[k])+1
		w=b-l
		m=m+w
		k=k-1
	print m	