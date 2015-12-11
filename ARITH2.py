def operate(a):
	if a[1]=="+":
		return str(int(a[0])+int(a[2]))
	elif a[1]=="-":
		return str(int(a[0])-int(a[2]))
	elif a[1]=="*":
		return str(int(a[0])*int(a[2]))
	else:
		return str(int(a[0])/int(a[2]))


t=int(raw_input())
for i in range(t):
	raw_input()
	a=raw_input()
	b=[]
	c=[]
	for ch in a:
		if ch!=" "
			b.append(ch)
	while len(b)!=0:
		if b[0]==" ":
			b.pop(0)
		else:
			c.append(b.pop(0))
			#print len(c)
			if len(c)==3:
				print c
				b.insert(0,operate(c))
				c=[]
	print int(c[0])
	
