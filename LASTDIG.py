t=int(raw_input())
for i in range(t):
	x=map(int,raw_input().split())
	a=[]
	for j in range(1,5):
		a.append((x[0]**j)%10)
	
	for k in range(1,5):
		if x[1]%4==0:
			if x[1]==0:
				print 0
				break
			else:	
				print a[3]
				break
		else:
			if x[1]%4==k:
				print a[k-1]
				break