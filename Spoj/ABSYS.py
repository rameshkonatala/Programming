def check(x):
	b=[str(i) for i in x]
	t=1
	for j in range(len(b)):
		if b[j]=="m":
			t=0
			break
	if t==0:
		return 0
	else:
		return 1
	
t=int(raw_input())
for i in range(t):
	raw_input()
	a=raw_input().split()
	for j in (0,2,4):
		if check(a[j])==0:
			s=j
			break
	
	if s==4:
		a[s]=str(int(a[0])+int(a[2]))
		print " ".join(a)
	else:
		a[s]=str(int(a[4])-int(a[abs(2-s)]))
		print " ".join(a)