a,b=map(int,raw_input().split())
while a!=-1 and b!=-1:
	if a>b:
		c=a
		a=b
		b=c
	if a==0:
		print b
	else:
		print max(b/a,b%a)
	a,b=map(int,raw_input().split())