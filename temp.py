while(1):
    n = int(input())
    if(n==0): break
    temp=[]
    flag = True
    arr = [ int(x) for x in input().split()]
    for idx, val in enumerate(arr):
        if(arr[val-1] != idx + 1):
            flag=False
            break
 
    print flag