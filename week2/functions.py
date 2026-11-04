# name = "Deepak"

# def greet():
#     # name = "varsha"
#     return "Hello "+name

# print(greet())


# counter = 0 
# def increment():
#     global counter
#     counter = counter+1 
#     return counter

# print(increment())
# print(increment())
# print(increment())
# print(increment())
# print(counter)

# def outer():
#     count = 0 
#     def inner():
#         nonlocal count 
#         count += 1 
#     inner()
#     inner()
#     print(count)

# outer()

# n = 10 

# def increment(n):
#     n+=1 
#     return n 

# increment(n)

# print(n)


# l = [1,2,3,4]

# def add_item(l,item):
#     l.append(item)
#     return l


# print(l)

# add_item(l,item=5)

# print(l)



# def total(*args):
#     print(args)
#     print(type(args))
#     return sum(args)


# print(total(1,2,3,4,5,6,7,8,9,10))

# l = []

# def add_friends(*args):
#     print(args)
#     for i in args:
#         l.append(i)
     
# print(add_friends("Deepak","Varsha","Stuthi","bunny"))




def print_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")

print_details(name="deepak",city="kakinada")

