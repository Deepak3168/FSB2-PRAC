### DICT 


details = {
    "name": "deepak",
    "age":23,
    "roll_no":26,
    "city":"Kakinada"
}
print(type(details))

print(details["name"])


print(details["age"])


print(details["roll_no"])

print(details["city"])


# adding an element in dict 

details["dob"] =  "26/12/2001"

print(details["dob"])


### Updating the element in a dict 

details["city"] = "Rajamahendravaram"

print(details)

# delete an element from dict

del details["dob"]

print(details)




