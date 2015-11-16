a,b,c=map(int,raw_input().split())
while a!=0 and b!=0 and c!=0:
	if b-a==c-b:
		print "AP",c+(b-a)
	else:
		print "GP",(c*b)/a
	a,b,c=map(int,raw_input().split())