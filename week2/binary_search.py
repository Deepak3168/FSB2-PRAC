
## Binary Search 

l = [2,7,9,11,23,35,47,56,62,72,88,92,102,112,122,132,142,152,162,172,182,192,202,212,222,232,242,252,262,272,282,292,302]
print(len(l))
target = 112
low = 0
high = len(l)-1 

while low<=high : 
    mid = (low+high)//2 
    print("mid",mid)
    print("high",high)
    print("low",low)
    print("element at mid",l[mid])
    if l[mid] == target :
        print(mid)
        break
    elif l[mid]  >  target : 
        high = mid - 1 
    else:
        low  = mid + 1 


