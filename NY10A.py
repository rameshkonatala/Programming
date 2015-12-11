t=int(raw_input())
for i in range(t):
	p=int(raw_input())
	x=raw_input()
	a=[]
	for j in x:
		a.append(j)
	m=['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']
	l=[0,0,0,0,0,0,0,0]
	for j in range(38):
		c=a[j:j+3]
		
		r=m.index("".join(c))
		l[r]=l[r]+1
		#print l
	l.insert(0,p)
	print " ".join(str(k) for k in l)