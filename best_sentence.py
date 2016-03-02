import random

def generateOne(strlen):
	alphabet="abcdefghijklmnopqrstuvwxyz "
	res=""
	for i in range(strlen):
		res = res + alphabet[random.randrange(27)]

	return res

def score(goal,teststring):
	numSame = 0
	for i in range(len(goal)):
		if goal[i]==teststring[i]:
			numSame = numSame+1
	return float(numSame)/ len(goal)

def main():
	goalstring = "this is ramesh"
	newstring = generateOne(len(goalstring))
	best = 0
	newscore = score(goalstring,newstring)
	while newscore<1:
		if newscore>best:
			print newscore,newstring
			best=newscore
		newstring=generateOne(len(goalstring))
		newscore= score(goalstring,newstring)

main()