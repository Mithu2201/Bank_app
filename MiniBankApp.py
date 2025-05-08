
import datetime
from tabulate import tabulate

def Create_user():

    print("============User details============")
    name=input("Enter Customer Name-(Ex-John) :")
    ph_no=int(input("Enter Contact number-(Ex-07X-1234567) :"))
    Address=input("Enter Customer Address-(Ex-Jaffna) :")
    user=input("Enter User Name -(Ex-Marco123@) :")
    Pass_w=input("Enter Password-(Ex-User@123) :")
    date=datetime.datetime.now()
    
    User1[name]={
        'phone_no' : ph_no,
        'place'    : Address,
        'user_id' : user,
        'password' : pass_w,
        'Date': date.strftime("%Y-%m-%d- %H:%M:%S")
    }

    print("Your Profile has been Created")
    
    print(": Name          : Phone_NUmber  : Address       : User_ID       : Password      : Date                     :")
    for user_id,details in User1.items():
                
        print(":",user_id," " *(12-len(user_id)),":",details['phone_no']," " *(12-len(str(details['phone_no']))),":",details['place']," " *(12-len(details['place'])),":",details['user_id']," " *(12-len(str(details['user_id']))),":",details['password']," " *(12-len(str(details['password']))),":",details['Date']," " *(18-len(str(details['Date']))),)

    with open("customers.txt", "a") as file:
        file.write(f"{user_id}\t{details['phone_no']}\t{details['place']}\t{details['user_id']}\t{details['password']}\t{details['Date']}\t\n")
    
    return User1


def load_users(filename="customers.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 6:
                    name = parts[0]
                    ph_no = int(parts[1])
                    address = parts[2]
                    user = parts[3]
                    pass_w = parts[4]
                    date = parts[5]
                    loaded_data[name] = {
                        'phone_no': ph_no,
                        'address': address,
                        'user_id': user,
                        'password': pass_w,
                        'Date': date
                    }
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    return loaded_data

def find_user(Customer):
    
    seek_id=input("Enter user ID : ")
    if seek_id in Customer:
        print("User Found:")
        x=Customer[seek_id]
        print("Password  : Address    : phone_num        : Date           :")
        print('         '.join(str(value)for value in x.values())) 
        
    else:
        print("User not found.")

def create_Account(User2=None):
    if User2 is None:
        User2 = {}

    print("===========Account details===========")
    
    Name=input("Enter Customer Name-Ex-(Jana) :")
    Acc_type=input("Enter Account Type-(Ex-Saving/Current/Fixed) :")
    Intial_bal=float(input("Enter Intial Balance: "))
    date=datetime.datetime.now()
    print("Your Account has been Created with",Intial_bal)
    Acc_no = Auto_Acc_no()
    print(f"Your Account Number is: {Acc_no}")

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

def Auto_Acc_no(filename="accounts.txt"):
    max_acc_no = 999  # start before the first valid account number
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if parts and parts[0].isdigit():
                    acc_no = int(parts[0])
                    if acc_no > max_acc_no:
                        max_acc_no = acc_no
    except FileNotFoundError:
        pass  # file doesn't exist yet, so we start at 1000

    return max_acc_no + 1

def find_acc(User_Acc):
    
    seek_id=int(input("Enter Account number : "))
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

def history(account_name=None):
    print("Transaction History:\n")

    transactions = []

    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                parts = [item.strip() for item in line.split('\t')]
                if len(parts) == 6:
                    if account_name is None or parts[0] == account_name:
                        transactions.append(parts)
                else:
                    print(f"Skipping malformed line: {line}")
    except FileNotFoundError:
        print("Transaction file not found.")
        return

    # Print the table
    headers = ["Customer_name", "Account_Type", "Transaction Amount","Status", "Close Balance", "Date"]
    if transactions:
        print(tabulate(transactions, headers=headers))
    else:
        print("No transactions found for this account.")

def exit():
    
    print("Thank for using our service")

while True:

    U_name="HI"
    P_word="123"
    Us_name="go"
    Pa_word="456"
    User1={}
    User2={}

    print("=========Login Menu=========")
    print("1.Admin")
    print("2.Customer")
    print("3.Log out")

    pick=int(input("Choose an Option :"))
    
    if pick==3:
        print("Logging out")
        break

    user=(input("Enter Your User Name :"))
    pass_w=(input("Enter Your Password :"))

    if pick==1 and user==U_name and pass_w==P_word:

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

                users = load_users()
                print(users)
                find_user(users)
            
            elif select==3:

                User_Acc=create_Account()
                
                print("Account_Number  : Customer_name : Account_Type    : Open_balance       : Date                     :")
                for user_id,details in User_Acc.items():
                    
                    print(":",user_id," " *(12-len(str(user_id))),":",details['Name']," " *(12-len(str(details['Name']))),":",details['Account_type']," " *(12-len(details['Account_type'])),":",details['Opening_bal']," " *(12-len(str(details['Opening_bal']))),":",details['Date']," " *(18-len(str(details['Date']))),)

                with open("accounts.txt", "a") as file:
                        file.write(f"{user_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

            elif select==4:

                accounts = load_accounts()
                print(accounts)

                find_acc(accounts)

            elif select==5:
                status="Deposit"
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
                    file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{status}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")

                with open("accounts.txt", "w") as file:
                        for acc_id, details in accounts.items():
                            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
                
            elif select==6:
                status1="Withdraw"
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
                print(accounts)
                date=datetime.datetime.now()

                with open("transactions.txt", "a") as file:
                    file.write(f"{a_name}\t{a_num}\t{dip_amount}\t{status1}\t{open_bal}\t{date.strftime("%Y-%m-%d-%H:%M:%S")}\t\n")

                with open("accounts.txt", "w") as file:
                        for acc_id, details in accounts.items():
                            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
                
            elif select==7:
                
                accounts = load_accounts()
                print(accounts)
                
                final=get_Bal(accounts)

            elif select==8:

                history()

                name = input("Enter Customer name to view history: ")
                history(name)

            elif select==9:
                exit()
                break

    elif pick==2 and user==Us_name and pass_w==Pa_word:

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
                
                with open("accounts.txt", "w") as file:
                        for acc_id, details in accounts.items():
                            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
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

                with open("accounts.txt", "w") as file:
                        for acc_id, details in accounts.items():
                            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

            elif select==4:
                
                accounts = load_accounts()
                print(accounts)
                
                final=get_Bal(accounts)

            elif select==5:
                
                name = input("Enter Your name to view history: ")
                history(name)

            elif select==6:
                exit()
                break
    else:
        print("User name and Password are incorrect, Enter correctly")
            

