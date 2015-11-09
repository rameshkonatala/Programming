t=int(raw_input())
b=[]
for i in range(t):
	n=int(raw_input())
	if n%2==0:
		b.append(n-(n/2)+1)
	else:
		b.append(n-(n/2))

for i in range(t):
	print b[i]
	