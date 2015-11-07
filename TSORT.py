t=int(raw_input())
x=[]
for i in range(t):
	n=int(raw_input())
	x.append(n)
				
			
for i in range(1,t):
	while i>0 and x[i]<x[i-1]:
		temp=x[i]
		x[i]=x[i-1]
		x[i-1]=temp
		i=i-1
		
for i in range(t):
		print x[i]
		