t=int(raw_input())
a=[2048,1024,512,256,128,64,32,16,8,4,2,1]

for i in range(t):
	n=int(raw_input())
	r=0
	for j in range(12):
		if (n%a[j])==0:
			r=r+(n/a[j])
			break
			
		else:
			r=r+(n/a[j])
			n=n%a[j]
	print r
			
	
		