# STRING 


# CREATION 
# name = "Stuthi"


# name2 = name.replace("t","T")

# print(name)

# print(name2)


# name = "Stuthi"
# name2 = ""

# for i in name :
#     if i=='t':
#         name2 += "T"
#     else:
#         name2 += i 

# print(name2)




name = "Varsha"

upper_case_name = ""


for i in name : 
    if ord(i) >= 65 and ord(i) <= 90 : 
        upper_case_name += i 
    elif ord(i) >=97 and ord(i) <= 122 :
        upper_case_name += chr(ord(i)-32)

print(name)
print(upper_case_name)
