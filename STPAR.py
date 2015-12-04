p=int(raw_input())
while p!=0:
	to=[]
	bet=[]
	fro=map(int,raw_input().split())
	j=0
	fro.reverse()
	x=len(fro)
	t=1
	while t!=0 and len(to)!=x:
		if len(fro)!=0 and fro[len(fro)-1]==(j+1):
			to.append(fro.pop())
			j=j+1
			#print "from fro to to",to
		elif len(bet)!=0 and bet[len(bet)-1]==(j+1):
			to.append(bet.pop())
			j=j+1
			#print "from bet to to",to
		else:
			if len(fro)!=0:
				bet.append(fro.pop())
				#print "from fro to bet",bet
			if len(bet)>1 and bet[len(bet)-1]>bet[len(bet)-2]:
				t=0
		

	if t==0:
		print "No"
	else:
		print "Yes"

	p=int(raw_input())	