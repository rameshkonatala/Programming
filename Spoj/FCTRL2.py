def fact(x):
	while x!=1:
		return x*fact(x-1)
	else:
		return 1

		
t=int(raw_input())
for i in range(t):
	n=int(raw_input())
	a=fact(n)
	print a