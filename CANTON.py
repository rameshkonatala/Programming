t=int(raw_input())
for i in range(t):
	k=int(raw_input())
	if k==1:
		
		print "TERM %d IS 1/1" %(k)
	else:
		n=1
		while (n*(n+1))/2 < k:
			s=(n*(n+1))/2
			n=n+1
		a=k-s
		if n%2!=0:
			print "TERM %d IS %d/%d" %(k,n+1-a,a)
		else:
			print "TERM %d IS %d/%d" %(k,a,n+1-a)