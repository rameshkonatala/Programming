p=int(raw_input())
for i in range(p):
	q=str(raw_input())
	r=int(raw_input())
	c=0
	for j in range(r):
		c=c+int(raw_input())
	if c%r==0:
		print 'yes'
	else:
		print 'no'