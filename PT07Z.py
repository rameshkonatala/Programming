def insertionsort2(alist):
	for index in range(2,len(alist),2):
		currentvalue=alist[index]
		currentvalue2=alist[index+1]
		position=index
		position2=index+1
		while position>0 and alist[position-2]>currentvalue:
			alist[position]=alist[position-2]
			alist[position2]=alist[position2-2]
			position=position-2
			position2=position2-2
		alist[position]=currentvalue
		alist[position2]=currentvalue2
		
def branch(lis):
	
	lis.pop()
	l=lis.pop()
	j=len(lis)
	while j!=0:
		if l==lis[j-1]:
			lis.pop(j-1)
			l=lis.pop(j-2)
			j=len(lis)
		else:
			j=j-2
			
	return lis
	
t=int(raw_input())
main=[]
for i in range(t-1):
	main=main+(map(int,raw_input().split()))

insertionsort2(main)
#print main

branchlis=[]
while len(main)!=0:
	beforelen=len(main)
	main=branch(main)
	#print main
	afterlen=len(main)
	lenbranch=(beforelen-afterlen)/2
	branchlis.append(lenbranch)
	#print branchlis
	
print max(branchlis)
		