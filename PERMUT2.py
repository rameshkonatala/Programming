while(1):
	n = int(input())
	if n==0:
		break
	
		
	a=[int(x) for x in raw_input().split()]
	t=1

	for i in range(len(a)):
		if a[a[i]-1]!=i+1:
			t=2
			break
			
	if t==2:
		print "not ambiguous"
	else:
		print "ambiguous"

	
