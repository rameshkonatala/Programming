t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    flag=0 
    while(n!=0):
       flag+=int(n/5)
       n=int(n/5)
    print flag