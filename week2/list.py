#### LIST 

#### CREATE 

l = [1,2,3,4,5,6]


#### READ 

print(l[0])
print(l[1])


print("Loop Start")

for i in l: 
    print(i)


print("Range loop Start")

for i in range(6):
    print(l[i])

#### UPDATE LIST


# ADDDING AT THE END OF THE LIST 
l.append(7) #O(1)

print(l)


# ADDDING AT THE BEGINING OF THE LIST 

l.insert(0,9)  # O(n)

print(l)

# ADDING AT THE nth POSITION OF THE LIST
l.insert(5,8) # O(n)

print(l)

#REPLACING AN EXISTING ELEMENT 

l[2] = 4 # O(1)

print(l)



k = [3,4,5]

l.extend(k)


print(l)


### DELETE 

# Delete At the End of the list 

print(l.pop())

print(l)

## DELETE AT THE Nth position of the element 

l.remove(8)

print(l)

del l[5]

print(l)


print(len(l))
print(sum(l))
print(max(l))
print(min(l))