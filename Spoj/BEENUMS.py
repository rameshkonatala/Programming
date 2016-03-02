from math import sqrt
t=int(raw_input())
while t!=-1:
	a=9+sqrt(9-(12*(1-t)))
	b=9-sqrt(9-(12*(1-t)))
	if (a%6==0 and a/6>0) or (b%6==0 and b/6>0) :
		print "Y"
	else:
		print "N"
	t=int(raw_input())