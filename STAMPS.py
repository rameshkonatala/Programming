t=int(raw_input())
for i in range(t):
	a,b=map(int,raw_input().split())
	x=map(int,raw_input().split())
	s=0
	for j in range(len(x)):
		s=s+x[j]
	if s<a:
		print "Scenario #"+str(i+1)+":"
		print "impossible"
	else:
		x.sort()
		
		y=0
		k=0
		z=len(x)
		while y<a:
			y=y+x[z-1]
			k=k+1
			z=z-1
			
		print "Scenario #"+str(i+1)+":"
		print k