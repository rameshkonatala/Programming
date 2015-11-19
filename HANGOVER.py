from fractions import Fraction
t=float(raw_input())
while t!=0.00:
	s=0.00
	i=1
	while s<=t:
		a=Fraction(1,i+1)
		s=s+float(a)
		i=i+1
	print i-1,"card(s)"
	t=float(raw_input())