import fractions
a,b,c=map(int,raw_input().split())
while a!=0 or b!=0 or c!=0:
	if b-a==c-b:
		print "AP",c+(b-a)
	else:
		f=fractions.Fraction(c*b,a)
		print "GP",f
	a,b,c=map(int,raw_input().split())