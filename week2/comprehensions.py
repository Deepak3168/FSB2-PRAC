# list comprehensions 


l = [ x**2 for x in range(10) if x%2==0 ]


fruits= ["apple","bananna","mango","guava"]

u  = { len(x) for x in fruits }

print(u)

d = {word : len(word) for word in fruits}

print(d)