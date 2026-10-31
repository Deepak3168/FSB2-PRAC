## 123 1+2+3 = 6 


n =  int(input("Enter a number"))

total = 0 
i = 1
while n > 0 : 
    print(i ,"at iteration n value  ", n)
    d = n%10 
    print(i,"at iteration digit value ", d)
    total += d
    print(i,"at iteration  total value "  , total)
    n //= 10
    i+=1 


print(total)
