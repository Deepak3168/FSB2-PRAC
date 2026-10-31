l = [12,34,56,77,5,9,34,75]


max_ = l[0]

for i in range(1,len(l)):
    if l[i] > max_ : 
        max_ = l[i]


print(max_)
