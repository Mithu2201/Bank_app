# while True:

#     U_name="HI"
#     P_word="123"
#     Us_name="go"
#     Pa_word="456"

#     print("=========Login Menu=========")
#     print("1.Admin")
#     print("2.Customer")
#     print("3.Log out")

#     pick=int(input("Choose an Option :"))
    
#     if pick==3:
#         print("Logging out")
#         break

#     user=(input("Enter Your User Name :"))
#     pass_w=(input("Enter Your Password :"))

#     if pick==1 and user==U_name and pass_w==P_word:
#         print("HI")

#     elif pick==2 and user==Us_name and pass_w==Pa_word:
#         print("bye")

#     else:
#         print("User name and Password are incorrect, Enter correctly")



#Deactivate User

def delete_user(filename="customers.txt"):
    users = load_users(filename)
    del_name = input("Enter the name of the user to delete: ")

    if del_name in users:
        del users[del_name]
        print(f"User '{del_name}' has been deleted.")
        
        # Rewrite the file without the deleted user
        with open(filename, "w") as file:
            for name, details in users.items():
                file.write(f"{name}\t{details['phone_no']}\t{details['address']}\t{details['user_id']}\t{details['password']}\t{details['Date']}\n")
    else:
        print(f"User '{del_name}' not found.")

#Deactivate Accounts
