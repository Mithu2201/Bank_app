
import datetime
from tabulate import tabulate
import os

def Create_user(): #create new customer 

    print("============User details============")
    name=input("Enter Customer Name-(Ex-John) :")
    while True: #validate phone number input
        try:
            ph_no = int(input("Enter Contact Number (Ex-0712345678): "))
            break
        except ValueError:
            print("Invalid number. Please enter digits only.")
    Address=input("Enter Customer Address-(Ex-Jaffna) :")
    user=input("Enter User Name -(Ex-Marco123@) :")
    Pass=input("Enter Password-(Ex-User@123) :")
    date=datetime.datetime.now()
    #save user detail to dictionary   
    User1[name]={
        'phone_no' : ph_no,
        'place'    : Address,
        'user_id' : user,
        'password' : Pass,
        'Date': date.strftime("%Y-%m-%d- %H:%M:%S")
    }

    print("Your Profile has been Created")
    #print created customer
    print(": Name          : Phone_NUmber  : Address       : Date                     :")
    for user_id,details in User1.items():
        print(":",user_id," " *(12-len(user_id)),":",details['phone_no']," " *(12-len(str(details['phone_no']))),":",details['place']," " *(12-len(details['place'])),":",details['Date']," " *(18-len(str(details['Date']))),)
    #save txt files
    with open("customers.txt", "a") as file:
        file.write(f"{user_id}\t{details['phone_no']}\t{details['place']}\t{details['Date']}\t\n")

    with open("users.txt", "a") as file:
        file.write(f"{details['user_id']}\t{details['password']}\t\n")
#load customer details from file
def load_users(filename="customers.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 4:
                    name = parts[0]
                    ph_no = int(parts[1])
                    address = parts[2]
                    date = parts[3]
                    loaded_data[name] = {
                        'phone_no': ph_no,
                        'address': address,
                        'Date': date
                    }
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    return loaded_data
#load customers user name password to provide login
def load_admins(filename="users.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    user = parts[0]
                    pass_word = parts[1]
                    loaded_data[user] = pass_word
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    return loaded_data
#search user by name
def find_user(Customer):
    while True:
        try:
            seek_id=input("Enter user name : ")
            break
        except ValueError:
            print("Invalid name. Please enter correct one.")
    
    if seek_id in Customer:
        print("User Found:")
        x=Customer[seek_id]
        print("phone_num        : Address    : Date           :")
        print('         '.join(str(value)for value in x.values())) 
        
    else:
        print("User not found.")
#create a bank account and save into files
def create_Account(User2=None):
    if User2 is None:
        User2 = {}

    print("===========Account details===========")
    
    Name=input("Enter Customer Name-Ex-(Jana) :")
    Acc_type=input("Enter Account Type-(Ex-Saving/Current/Fixed) :")
    while True:
        try:
            Intial_bal=float(input("Enter Intial Balance: "))
            break
        except ValueError:
            print("Invalid number. Please enter number only.")
    date=datetime.datetime.now()
    print("Your Account has been Created with",Intial_bal)
    Acc_no = Auto_Acc_no()
    print(f"Your Account Number is: {Acc_no}")
    #save user detail to dictionary     
    User2[Acc_no]={
        'Name' : Name,
        'Account_type' : Acc_type,
        'Opening_bal' : Intial_bal,
        'Date'      : date.strftime("%Y-%m-%d- %H:%M:%S")
    }
    #print created account
    print("Account_Number  : Customer_name : Account_Type    : Open_balance       : Date                     :")
    for user_id,details in User2.items():
        
        print(":",user_id," " *(12-len(str(user_id))),":",details['Name']," " *(12-len(str(details['Name']))),":",details['Account_type']," " *(12-len(details['Account_type'])),":",details['Opening_bal']," " *(12-len(str(details['Opening_bal']))),":",details['Date']," " *(18-len(str(details['Date']))),)
    #save to accounts file
    with open("accounts.txt", "a") as file:
            file.write(f"{user_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

# Load accounts from file
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
# Generate a new unique account number
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
# Find account by account number
def find_acc(User_Acc):
    while True:
        try:
            seek_id=int(input("Enter Account number : "))
            break
        except ValueError:
            print("Invalid number. Please enter Existing one.")
    if seek_id in User_Acc:
        print("User Found:")
        dict_val=User_Acc[seek_id]
        print("Customer_name  : Account_Type    : Balance        : Date           :")
        print('         '.join(str(value)for value in dict_val.values())) 
        return dict_val
    else:
        print("User not found.")
# Deposit money to account
def deposit():
    accounts = load_accounts()

    rece=find_acc(accounts)
    a_name=rece['Name']
    a_num=rece['Account_type']
    open_bal=rece['Opening_bal']

    while True:
        try:
            amount=float(input("Enter Deposit Amount :"))
        except ValueError:
            print("Invalid number. Please enter number only.")

        if  amount>0:

            open_bal+=amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            date=datetime.datetime.now()
            # record transaction
            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{amount}\tDeposit\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")
            # Update accounts
            with open("accounts.txt", "w") as file:
                    for acc_id, details in accounts.items():
                        file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
            break
        else:
            print("Negative or zero amount")
# Withdraw money from account         
def withdraw():
    accounts = load_accounts()
                    
    rece=find_acc(accounts)
    a_name=rece['Name']
    a_num=rece['Account_type']
    open_bal=rece['Opening_bal']

    while True:
        try:
            amount=float(input("Enter Withdraw Amount :"))
        except ValueError:
            print("Invalid number. Please enter number only.")

        if 0 < amount and amount <= rece['Opening_bal']:
                
            open_bal-=amount
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            date=datetime.datetime.now()
            # record transaction
            with open("transactions.txt", "a") as file:
                file.write(f"{a_name}\t{a_num}\t{amount}\tWithdraw\t{open_bal}\t{date.strftime("%Y-%m-%d-%H:%M:%S")}\t\n")
            # Update accounts
            with open("accounts.txt", "w") as file:
                    for acc_id, details in accounts.items():
                        file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
            break
        else:
            print("Withdrawals greater than the balance")   
        
# Check balance
def get_Bal(User_Acc):
    while True:
        try:
            seek_id=int(input("Enter Account number : "))
            break
        except ValueError:
            print("Invalid number. Please enter number only.")
    
    if seek_id in User_Acc:
        print("User Found:")
        dict_val=User_Acc[seek_id]
        print("Customer_name  : Pho_number    : Address        : Date           :")
        print('         '.join(str(value)for value in dict_val.values())) 
        return dict_val
    else:
        print("User not found.")
# Show transaction history
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
# Transfer money between accounts
def transfer_money(accounts):
    print("======== Money Transfer ========")
    
    try:
        sender_id = int(input("Enter Sender Account Number: "))
        receiver_id = int(input("Enter Receiver Account Number: "))
    except ValueError:
        print("Invalid input. Account numbers must be numeric.")
        return

    if sender_id not in accounts or receiver_id not in accounts:
        print("Sender or receiver account not found.")
        return

    sender = accounts[sender_id]
    receiver = accounts[receiver_id]

    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return
        if amount > sender['Opening_bal']:
            print("Insufficient funds in sender's account.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    # Perform transaction
    sender['Opening_bal'] -= amount
    receiver['Opening_bal'] += amount
    print("Transfer successful.")

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log transaction for sender
    with open("transactions.txt", "a") as file:
        file.write(f"{sender['Name']}\t{sender['Account_type']}\t{amount}\tDeposit\t{sender['Opening_bal']}\t{date}\n")
        file.write(f"{receiver['Name']}\t{receiver['Account_type']}\t{amount}\twithdraw\t{receiver['Opening_bal']}\t{date}\n")

    # Update accounts file
    with open("accounts.txt", "w") as file:
        for acc_id, details in accounts.items():
            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
# Add monthly interest to all accounts
def add_interest(accounts):
    print("====== Add Interest to Accounts ======")
    interest_rate=float(input("Enter Interest for current Month % :"))
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for acc_id, acc in accounts.items():
        acc_type = acc['Account_type']
        if acc_type in ['saving', 'fixed','current']:
            current_balance = acc['Opening_bal']
            interest = current_balance * interest_rate
            acc['Opening_bal'] += interest
            print(f"Interest of {interest:.2f} added to account {acc_id} {acc['Name']}")

            # recoard interest transaction
            with open("transactions.txt", "a") as file:
                file.write(f"{acc['Name']}\t{acc['Account_type']}\t{interest:.2f}\tInterest\t{acc['Opening_bal']:.2f}\t{date}\n")


    with open("accounts.txt", "w") as file:
        for acc_id, details in accounts.items():
            file.write(f"{acc_id}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']:.2f}\t{details['Date']}\n")
def exit(): # Exit message
    
    print("Thank for using our service")

while True:

    if not os.path.exists("users.txt"):
        with open("users.txt", "a") as file:
            file.write("Admin\t123\n") 
    admins=load_admins()

    User1={}
    User2={}

    print("=========Login Menu=========")
    print("1.Admin")
    print("2.Customer")
    print("3.Log out")
    while True:
        try:
            pick=int(input("Choose an Option :(1-3)"))
            break
        except ValueError:
            print("Invalid number. Please enter correct number.")
    
    
    if pick==3:
        print("Logging out")
        break

    username = input("Enter Your User Name : ")
    password = input("Enter Your Password : ")

    if pick==1: 
        if username in admins and admins[username] == password:

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
                print("9.Transfer Money")
                print("10.Add intrest")
                print("11.Exit")
                while True:
                    try:
                        select=int(input("Choose an Option(1-11) :"))
                        break
                    except ValueError:
                        print("Invalid number. Please enter correct number.")
                
                
                if select==1:
                    Create_user()
                    
                elif select==2:
                    users = load_users()
                    find_user(users)
                    
                elif select==3:
                    create_Account()

                elif select==4:
                    accounts = load_accounts()
                    find_acc(accounts)

                elif select==5:
                    deposit()
                    
                elif select==6:
                    withdraw()

                elif select==7:
                    accounts = load_accounts()
                    final=get_Bal(accounts)

                elif select==8:
                    history()
                    name = input("Enter Customer name to view history: ")
                    history(name)

                elif select==9:
                    accounts = load_accounts()
                    transfer_money(accounts)
                
                elif select==10:
                    accounts = load_accounts()
                    add_interest(accounts)

                elif select==11:
                    exit()
                    break

    elif pick==2:
        if username in admins and admins[username] == password:

            while True:
                print("============Menu===========")    
                print("1.Create User")
                print("2.Deposit Money")
                print("3.Withdrw Money")
                print("4.Check balance")
                print("5.Transaction Histry")
                print("6.Transfer Money")
                print("7.Exit")
                while True:
                    try:
                        select=int(input("Choose an Option(1-7) :"))
                        break
                    except ValueError:
                        print("Invalid number. Please enter correct number.")
                
                
                if select==1:
                    Create_user()

                elif select==2:
                    deposit()

                elif select==3:
                    withdraw()
                    
                elif select==4:
                    accounts = load_accounts()
                    final=get_Bal(accounts)

                elif select==5:
                    name = input("Enter Your name to view history: ")
                    history(name)

                elif select==6:
                    accounts = load_accounts()
                    transfer_money(accounts)

                elif select==7:
                    exit()
                    break
        else:
            print("Customer not found.")
    
    else:
        print("User name and Password are incorrect, Enter correctly")
            

