a,b=map(int,raw_input().split())
while a!=0 and b!=0:
	l=map(int,raw_input().split())
	m=map(int,raw_input().split())
	lmin=min(l)
	m.sort()
	m.pop(0)
	mmin=m[0]
	if lmin<mmin:
		print "Y"
	else:
		print "N"
	a,b=map(int,raw_input().split())