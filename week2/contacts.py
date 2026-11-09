contacts = [
    {
        "name":"Deepak",
        "phone":"9131043168"
    },
    {
            "name":"Varsha",
            "phone":"9131043168"
        },
        {
                "name":"Stuthi",
                "phone":"9131043168"
            },
            {
                    "name":"Bunny",
                    "phone":"9131043168"
                }
]

def delete_contact(id):
    del contacts[id]



def list_contacts():
    for id,value in enumerate(contacts):
        print(id,value['name'])



print(list_contacts())

delete_contact(3)


print(list_contacts())


contacts[1]["name"] = "Naga sri Varsha"

print(list_contacts())




