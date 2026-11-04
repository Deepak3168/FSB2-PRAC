##  LC167

l = [2,3,4,11,15]


target = 26


low = 0 
high = len(l)-1



while low < high : 
    sum_ = l[low]+l[high] 
    if sum_ == target : 
        print(low+1,high+1)
        break 
    elif sum_ > target : 
        high -= 1 
    else :
        low += 1 

