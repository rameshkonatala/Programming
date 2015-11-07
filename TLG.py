t=int(raw_input())
x=[]
r=0
for i in range(t):
	a,b=(raw_input().split())
	p=int(a)
	q=int(b)
	r=r+(p-q)
	x.append(r)
	

print x
p=max(x)
q=min(x)


if p>abs(q):
	print 1,"",p
else:
	print 2,"",abs(q)
	