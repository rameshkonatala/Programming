t=int(raw_input())
for i in range(t):
	k=int(raw_input())
	if k==1:
		print "TERM",k,"IS",str(1)+str("/")+str(1)
	else:
		n=1
		while (n*(n+1))/2 < k:
			s=(n*(n+1))/2
			n=n+1
		a=k-s
		if n%2==0:
			print "TERM",k,"IS",str(n+1-a)+str("/")+str(a)
		else:
			print "TERM",k,"IS",str(a)+str("/")+str(n+1-a)