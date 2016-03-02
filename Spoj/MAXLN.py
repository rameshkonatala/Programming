t=int(raw_input())
for i in range(t):
	r=int(raw_input())

	x=(16*r*r)+1
	l=round((x/4.0),2)
	#print l
	print "Case %d: %.2f" %(i+1,l)
