	
def inver(alist):
	t=0
	for index in range(1,len(alist)):
		currentvalue=alist[index]
		position=index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position=position-1
			t=t+1
		alist[position]=currentvalue
	return t	
	
t=int(raw_input())
for i in range(t):
	raw_input()
	p=input()
	l=[]
	for j in range(p):
		l.append(input())
	print inver(l)	