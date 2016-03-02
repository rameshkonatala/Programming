def rev(a):
	b=[]
	for i in range(len(a)):
		b.append(str(a[len(a)-1-i]))
	j=0
	while t!=0:
		if b[j]!="0":
			break
		else:
			b.remove(b[j])
			
	return int("".join(b))	



t=int(raw_input())
for i in range(t):
	x,y=raw_input().split()
	x=[int (i) for i in (x)]
	y=[int (i) for i in (y)]
	print rev(str(rev(x)+rev(y)))
	