def triangle(x):
	if x==1:
		return 1
	elif x==2:
		return 5
	elif x==3:
		return 13
	else:
		if x%2==0:
			return 2+3*(int(triangle(x-1))-int(triangle(x-2)))
		else:
			return 3+3*(int(triangle(x-1))-int(triangle(x-2)))

t=int(raw_input())
for j in range(t):
	a=int(raw_input())
	print triangle(a)
