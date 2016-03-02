t=int(raw_input())
a=[]
for i in range(t):
	if i==0:
		a=int(raw_input())
		#a=bin(a)
		#print a
	else:
		b=int(raw_input())
		#b=bin(b)
		a= a^b
	
print a
