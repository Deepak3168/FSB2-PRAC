#zip
names = ['Varsha','Stuthi','Deepak']

scores = [99,96,95]

for name,score in zip(names,scores) :
    print(name,score)

#map

def square(x):
    return x**2 

nums = [1,2,3,5,6]

squared = map(square,nums)

print(list(squared))


doubled = list(map(lambda x:x*2 , nums))
print(doubled)


numbers = list(range(1,11))

def is_even(n):
    return n%2 == 0 

evens = filter(is_even,numbers)


print(list(evens))