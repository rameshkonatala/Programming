t=int(raw_input())
for i in range(t):
	s=int(raw_input())
	a=map(int,raw_input().split())
	b=map(int,raw_input().split())
	
	a.sort()
	b.sort()
	x=0
	
	for j in range(s):
		x=x+(a[j]*b[j])
	print x