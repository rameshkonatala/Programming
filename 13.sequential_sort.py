def orderedSequentialSearch(alist, item):
2	    pos = 0
3	    found = False
4	    stop = False
5	    while pos < len(alist) and not found and not stop:
6	        if alist[pos] == item:
7	            found = True
8	        else:
9	            if alist[pos] > item:
10	                stop = True
11	            else:
12	                pos = pos+1
13	
14	    return found
15	
16	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
17	print(orderedSequentialSearch(testlist, 3))
18	print(orderedSequentialSearch(testlist, 13))
