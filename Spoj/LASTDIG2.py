t=int(raw_input())
for i in range(t):
	a,b=map(int,raw_input().split())
	c=[]
	for j in range(4):
		c.append((a**(j+1))%10)
	if b==0:
		print 1
	else:
		p=b%4
		print c[p-1]