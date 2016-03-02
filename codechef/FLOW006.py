t=int(raw_input())
for i in range(t):
	a=[int (i) for i in (raw_input())]
	t=0
	for i in range(len(a)):
		t+=a[i]
	print t	