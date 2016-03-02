t=int(raw_input())
for i in range(t):
	a,b=map(int,raw_input().split())
	if a==0 and b==0:
		print "0"
	elif a-b<0 or a-b>2 or a-b==1 :
		print "No Number"
	else:
		if a%2==0:
			print a+b
			
		else:
			print a+b-1


		