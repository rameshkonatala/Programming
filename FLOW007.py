t=int(raw_input())
for i in range(t):
	a=[int (i) for i in (raw_input())]
	b=[]
	for i in range(len(a)):
		b.append(str(a[len(a)-1-i]))
	x=len(b)	
	for j in range(x):
		if b[j]!="0":
			
			print "A"
			break
		else:
			print "B"
			b.remove(b[j])
			x-=1
	print "".join(b)	