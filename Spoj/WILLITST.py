t=int(raw_input())
s=1
a=0
while 2**s<=t:
	if 2**s==t:
		a=1
		break
	else:
		s=s+1
if a==0:
	print "NIE"
else:
	print "TAK"