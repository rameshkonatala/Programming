t=int(raw_input())
l=1
for i in range(t):
	if t<i*i:
		l=i
		break

c=0		
for j in range(1,l):
	for k in range(j,t+1):
		if j*k>t:
			break
		else:
			c=c+1

print c