
import datetime
from tabulate import tabulate

def Create_user():

    print("============User details============")
    User_N=input("Enter User Name no-Ex-Marco123@ :")
    Pas_w=input("Enter Password-Ex-User@123 :")
    ph_no=int(input("Enter user contact no-Ex-0771234567 :"))
    Address=input("Enter user Address-Ex-Jaffna/Mullaithivu :")
    date=datetime.datetime.now()
    
    User1[User_N]={

        'password' : Pas_w,
        'phone_num' : ph_no,
        'place'    : Address,
        'Date': date.strftime("%Y-%m-%d- %H:%M:%S")
    }

    print("Your Profile has been Created")
    
    print("User_ID         : Password      : Pho_number    : Address       : Date                     :")
    for user_id,details in User1.items():
                
        print(":",user_id," " *(12-len(str(user_id))),
        ":",details['password']," " *(12-len(details['password'])),
        ":",details['phone_num']," " *(12-len(str(details['phone_num']))),
        ":",details['place']," " *(12-len(details['place'])),
        ":",details['Date']," " *(18-len(str(details['Date']))),)

    with open("customers.txt", "a") as file:
        file.write(f"{user_id}\t{details['password']}\t{details['phone_num']}\t{details['place']}\t{details['Date']}\t\n")
    
    return User1

def find_user(Customer):
    
    seek_id=int(input("Enter user ID : "))
    if seek_id in Customer:
        print("User Found:")
        x=Customer[seek_id]
        print("Password  : Address    : phone_num        : Date           :")
        print('         '.join(str(value)for value in x.values())) 
        
    else:
        print("User not found.")

def create_Account():

    print("===========Account details===========")
    Acc_no=int(input("Enter Account no-Ex-1000/1001 :"))
    Name=input("Enter Customer no-Ex-Jana/Periya :")
    Acc_type=input("Enter Account Type-Ex-Saving/Current/Fixed :")
    Intial_bal=float(input("Enter Intial Balance: "))
    date=datetime.datetime.now()
    print("Your Account has been Created with",Intial_bal)

    User2[Acc_no]={
        'Name' : Name,
        'Account_type' : Acc_type,
        'Opening_bal' : Intial_bal,
        'Date'      : date.strftime("%Y-%m-%d- %H:%M:%S")
    }
    return User2

def load_accounts(filename="accounts.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    acc_no = int(parts[0])
                    Name = parts[1]
                    acc_type = parts[2]
                    opening_bal = float(parts[3])
                    date = parts[4]
                    loaded_data[acc_no] = {
                        'Name': Name,
                        'Account_type': acc_type,
                        'Opening_bal': opening_bal,
                        'Date': date
                    }
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    return loaded_data

   
def find_acc(User_Acc):
    
    seek_id=int(input("Enter user ID : "))
    if seek_id in User_Acc:
        print("User Found:")
        dict_val=User_Acc[seek_id]
        print("Customer_name  : Pho_number    : Address        : Date           :")
        print('         '.join(str(value)for value in dict_val.values())) 
        return dict_val
    else:
        print("User not found.")

def deposit():
    try:
        amount=int(input("Enter Deposit Amount :"))
    
        if  amount>0:
            return amount
        else:
            print("Negative or zero amounts")

    except ValueError:
        print("Enter Digital value") 
        
def withdraw(balance):
    try:
        amount=int(input("Enter Withdraw Amount :"))

        if 0 < amount and amount <= balance:
            return amount 

        else:
            print("Withdrawals greater than the balance")
    except ValueError:
        print("Enter Digital value") 

def get_Bal(User_Acc):
    
    seek_id=int(input("Enter user ID : "))
    if seek_id in User_Acc:
        print("User Found:")
        dict_val=User_Acc[seek_id]
        print("Customer_name  : Pho_number    : Address        : Date           :")
        print('         '.join(str(value)for value in dict_val.values())) 
        return dict_val
    else:
        print("User not found.")

def history():
    print("Transaction History:\n")

    transactions = []

    with open("transactions.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            parts = [item.strip() for item in line.split('\t')]
            if len(parts) == 5:
                transactions.append(parts)
            else:
                print(f"Skipping malformed line: {line}")

    # Print the table
    headers = ["Customer_name", "Account_Type", "Transaction Amount", "Close Balance", "Date"]
    print(tabulate(transactions, headers=headers, tablefmt="grid"))

 
def exit():
    
    print("Thank for using our service")

U_name="HI"
P_word="123"
Us_name="go"
Pa_word="456"
User1={}
User2={}

user=(input("Enter Your User Name :"))
pass_w=(input("Enter Your Password :"))

if user==U_name and pass_w==P_word:

    while True:
        print("============Menu===========")    
        print("1.Create User")
        print("2.Search Customer")
        print("3.Create Account")
        print("4.Search Account")
        print("5.Deposit Money")
        print("6.Withdrw Money")
        print("7.Check balance")
        print("8.Transaction Histry")
        print("9.Exit")
        
        select=int(input("Choose an Option :"))
        
        if select==1:
            
            User1=Create_user()
            
        elif select==2:
        
            find_user(User1)
        
        elif select==3:

            User_Acc=create_Account()
            
            print("Account_Number  : Customer_name : Account_Type    : Open_balance       : Date                     :")
            for user_id,details in User_Acc.items():
                
                print(":",user_id," " *(12-len(str(user_id))),
                ":",details['Name']," " *(12-len(str(details['Name']))),
                ":",details['Account_type']," " *(12-len(details['Account_type'])),
                ":",details['Opening_bal']," " *(12-len(str(details['Opening_bal']))),
                ":",details['Date']," " *(18-len(str(details['Date']))),)

            with open("accounts.txt", "a") as file:
                    file.write(f"{user_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

        elif select==4:
            find_acc(User_Acc)

        elif select==5:
            accounts = load_accounts()
            print(accounts)
            
            rece=find_acc(accounts)
            a_name=rece['Name']
            a_num=rece['Account_type']
            open_bal=rece['Opening_bal']
            
            dip_amount=deposit()
            open_bal+=dip_amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            date=datetime.datetime.now()
            
            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")
            
        elif select==6:

            accounts = load_accounts()
            print(accounts)
            
            rece=find_acc(accounts)
            a_name=rece['Name']
            a_num=rece['Account_type']
            open_bal=rece['Opening_bal']
            
            dip_amount=withdraw(rece['Opening_bal'] )
            open_bal-=dip_amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal

            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{open_bal}\t{date.strftime("%Y-%m-%d-%H:%M:%S")}\t\n")
            
        elif select==7:
            
            accounts = load_accounts()
            print(accounts)
            
            final=get_Bal(accounts)

        elif select==8:

            history()

        elif select==9:
            exit()
            break

elif user==Us_name and pass_w==Pa_word:

    while True:
        print("============Menu===========")    
        print("1.Create User")
        print("2.Deposit Money")
        print("3.Withdrw Money")
        print("4.Check balance")
        print("5.Transaction Histry")
        print("6.Exit")
        
        select=int(input("Choose an Option :"))
        
        if select==1:
            
            User1=Create_user()

        elif select==2:
            
            accounts = load_accounts()
            print(accounts)
            
            rece=find_acc(accounts)
            a_name=rece['Name']
            a_num=rece['Account_type']
            open_bal=rece['Opening_bal']
            
            dip_amount=deposit()
            open_bal+=dip_amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            print(accounts)
            date=datetime.datetime.now()
            
            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")
            
        elif select==3:
            
            accounts = load_accounts()
            print(accounts)
            
            rece=find_acc(accounts)
            a_name=rece['Name']
            a_num=rece['Account_type']
            open_bal=rece['Opening_bal']
            
            dip_amount=withdraw(rece['Opening_bal'])
            open_bal-=dip_amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            print(accounts)
            date=datetime.datetime.now()

            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")

            
        elif select==4:
            
            accounts = load_accounts()
            print(accounts)
            
            final=get_Bal(accounts)

        elif select==5:
            
            history()

        elif select==6:
            exit()
            break
else:    
    print("Enter Correct User Name and password")
        

