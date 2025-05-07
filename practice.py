user = {
    "name": "kamal",
    "age": 25,
    "address": "jaffna"
}

#print dictionaries
""" print(user)
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items()) """

#print for lopp Dictionaries

""" for x in user:
    print(x)
    print(user[x])

for x in user:   
    print(x,"  ",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.keys():
    print(x,y)

if "age" in user:
    print("yes") """

#change key,values

""" user.update({"gender": "male"})
print(user)

user["age"]=35
print(user)

user.pop("age")

user = {
    "user01" : {
    "name": "kamal",
    "age": 25,
    "address": "jaffna"
    },
     "user02 ": {
    "name": "ram",
    "age": 30,
    "address": "kokuvil"
    },
     "user03" : {
    "name": "kamal",
    "age": 27 ,
    "address": "Meesalai"
    }
}

print(user) """

""" def biodata(**data)

    print(data)

biodata(name="mithu",age=45,gender="male") """

# nested_list = [
#     [1001,"Francis", "English", 435,"jaffna"],
#     [1002,"Larry","Maths", 234,"kopay"],
#     [1003,"Nicole", "Biology", 986,"sangupi"],
#     [1004,"Joey", "Physics", 562,"mannar"],
#     [1005,"Sam", "Computing", 12,"kilinoch"],
# ]

""" print(": First name : Subject     : Score :")

for item in nested_list:
    print(":",item[0]," " *(9-len(item[0])),":",
                    item[1]," " *(10-len(item[1])),":",
                    item[2]," " *(4-len(str(item[2]))),":")
nested_list.append(["kumar","maths",656])  """

#print(": Cutomer_name  : Nic_number  : Full_name   : Phone_num  : Address   :")

""" for item in nested_list:
    print(":",item[0]," " *(12-len(str(item[0]))),
            ":",item[1]," " *(10-len(item[1])),
            ":",item[2]," " *(10-len(item[2])),
            ":",item[3]," " *(9-len(str(item[3]))),
            ":",item[4]," " *(8-len(item[4])),":")
 """
# print(": Cutomer_ID  : Full_name   : Phone_num  : Address   :")

nested_list = {
    1001 :{'name' :"Francis", 'phone_no' : 771234567,'Address' :"jaffna"},
    1002 :{'name' :"Larry", 'phone_no' :778956234,'Address' :"kopay"},
    1003 :{'name' :"Nicole", 'phone_no' :772653986,'Address' :"sangupi"},
    1004 :{'name' :"Joey", 'phone_no' :778952562,'Address' :"mannar"},
    1005 :{'name' :"Sam", 'phone_no' :772541212,'Address' :"kilinoch"}
} 
# print("Full_name       Pho_number      Address")
# for user in nested_list.values():
#     print(f"{user['name']}\t\t{user['phone_no']}\t{user['Address']}")


"""     user,details=nested_list.items():
    print(f"{details['name']}\t\t{details['phone_no']}\t{details['Address']}") """


#print("Cutomer_ID  : Full_name   :    Phone_num  :      Address   :")

i=0
for i in nested_list:
    print(i)
    print(nested_list.keys())
    # for j in nested_list[i]:
    #     print(i,nested_list[i][j],end="      ")
    # print("\n")




