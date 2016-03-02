
t=int(raw_input())
for i in range(t):
	r=int(raw_input())
	p1,q1=map(int,raw_input().split())
	p2,q2=map(int,raw_input().split())
	p3,q3=map(int,raw_input().split())
	chc=float(((p1-p2)**2+(q1-q2)**2)**0.5)
	csc=float(((p1-p3)**2+(q1-q3)**2)**0.5)
	hcsc=float(((p2-p3)**2+(q2-q3)**2)**0.5)
	if chc<=r and csc<=r:
		print "yes"
	elif chc<=r or csc<=r:
		if hcsc<=r:
			print "yes"
		else:
			print "no"
	else:
		print "no"