t=int(raw_input())
for i in range(t):
	raw_input()
	raw_input()
	p=map(int,raw_input().split())
	q=map(int,raw_input().split())
	pmax=max(p)
	qmax=max(q)
	if pmax<qmax:
		print "MechaGodzilla"
	else:
		print "Godzilla"
		
		
		
		