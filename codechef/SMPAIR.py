t=int(raw_input())
for i in range(t):
	p=int(raw_input())
	a=map(int,raw_input().split())
	m=min(a)
	a.remove(m)
	n=min(a)
	a.remove(n)
	print m+n
	