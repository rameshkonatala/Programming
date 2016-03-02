import math
t=int(raw_input())
for i in range(t):
	a,b=raw_input().split()
	a,b=int(a),int(b)
	print math.sqrt((b**2)-(a**2)),math.sqrt((b**2)+(a**2))