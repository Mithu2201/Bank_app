import datetime
import os
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def Create_user(): #create new customer 
    User1={}
    existing_nics = set()
    existing_username=set()

    try:
        with open("customers.txt", "r") as file:
            for line in file:
                parts = line.strip().split("\t")
                if parts:
                    existing_nics.add(parts[0])
    except FileNotFoundError:
        pass 

    try:
        with open("users.txt","r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if parts:
                    existing_username.add(parts[0])
    except FileNotFoundError:
        pass

    print("============User details============")
    name=input("Enter Customer Name-(Ex-John) :").title()
    while True:
        nic = input("Enter NIC Number (Ex-2000123456): ")
        if len(nic) >= 10:
            if nic in existing_nics:
                print("This NIC already exists. Please use a different NIC.")
            else:
                break
        else:
            print("Invalid NIC. Must be at least 10 characters.")
    while True: #validate phone number input
        try:
            ph_no = int(input("Enter Contact Number (Ex-0712345678): "))
            break
        except ValueError:
            print("Invalid number. Please enter digits only.")
    Address=input("Enter Customer Address-(Ex-Jaffna) :")
    while True:
        user=input("Enter User Name -(Ex-Marco123@) :")
        if user in existing_username:
            print("name already exists")
        else:
            break
    Pass=input("Enter Password-(Ex-User@123) :")
    hashed_pass = hash_password(Pass)
    date=datetime.datetime.now()
    #save user detail to dictionary   
    User1[nic]={
        'name': name,
        'phone_no' : ph_no,
        'place'    : Address,
        'user_id' : user,
        'password' : Pass,
        'Date': date.strftime("%Y-%m-%d- %H:%M:%S")
    }

    print("Your Profile has been Created")
    #print created customer
    print(": NIC NUMBER   : Name        : Phone_NUmber  : Address       : Date                     ")
    for nic_id, details in User1.items():
        print(f": {nic_id:13}: {details['name']:12}: {details['phone_no']:14}: {details['place']:14}: {details['Date']}")
    #save txt files
    with open("customers.txt", "a") as file:
        file.write(f"{nic_id}\t{details['name']}\t{details['phone_no']}\t{details['place']}\t{details['Date']}\t\n")

    with open("users.txt", "a") as file:
        file.write(f"{details['user_id']}\t{hashed_pass}\t\n")

    with open("user_nic_map.txt", "a") as file:
        file.write(f"{details['user_id']}\t{nic_id}\n")
#load customer details from file
def load_users(filename="customers.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    nic = parts[0]
                    name = parts[1]
                    ph_no = int(parts[2])
                    address = parts[3]
                    date = parts[4]
                    loaded_data[nic] = {
                        'name': name,
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
            seek_id=input("Enter user NIC (Ex-2000123456): ")
            break
        except ValueError:
            print("Invalid NIC. Please enter correct one.")
    
    if seek_id in Customer:
        print("User Found:")
        x=Customer[seek_id]
        print(": Name             : phone_num        : Address    : Date           ")
        print('         '.join(str(value)for value in x.values())) 
        
    else:
        print("User not found.")
#create a bank account and save into files
def create_Account():
    User2 = {}
    existing_name = set()
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split("\t")
                if parts:
                    existing_name.add(parts[2])
    except FileNotFoundError:
        pass 
    print("===========Account details===========")
    
    while True:
        Name=input("Enter Customer Name-Ex-(Jana) :")
        if Name in existing_name:
            print("This name already exists. Please use a different name.")
        else:
            break
    while True:
        nic = input("Enter NIC Number (Ex-2000123456): ").strip()
        if len(nic) >= 10:
            break
        else:
            print("Invalid NIC. Must be at least 10 characters.")
    Acc_type=input("Enter Account Type-(Ex-saving/current/fixed) :")
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
        'NIC': nic,
        'Name' : Name,
        'Account_type' : Acc_type,
        'Opening_bal' : Intial_bal,
        'Date'      : date.strftime("%Y-%m-%d- %H:%M:%S")
    }
    #print created account
    print("Account_Number  : NIC Number  : Customer    : Account_Type  : Open_balance: Date                     ")
    for user_id,details in User2.items():
        print(f":{user_id:15}: {details['NIC']:12}: {details['Name']:12}: {details['Account_type']:14}: {details['Opening_bal']:12}: {details['Date']}")
    #save to accounts file
    with open("accounts.txt", "a") as file:
            file.write(f"{user_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

# Load accounts from file
def load_accounts(filename="accounts.txt"):
    loaded_data = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 6: 
                    acc_no = int(parts[0])
                    nic = parts[1]
                    name = parts[2]
                    acc_type = parts[3]
                    opening_bal = float(parts[4])
                    date = parts[5]
                    loaded_data[acc_no] = {
                        'NIC': nic, 
                        'Name': name,
                        'Account_type': acc_type,
                        'Opening_bal': opening_bal,
                        'Date': date
                    }
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    return loaded_data
# Generate a new unique account number
def Auto_Acc_no():
    max_acc_no = 999  # start before the first valid account number
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if parts and int(parts[0])>max_acc_no:
                        max_acc_no = int(parts[0])
    except FileNotFoundError:
        pass  # file doesn't exist yet, so we start at 1000

    return max_acc_no + 1
# Find account by account number
def find_acc(User_Acc):
    while True:
        try:
            seek_id=int(input("Enter Account number (Ex-1000) : "))
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
        return None
# Deposit money to account
def deposit():
    accounts = load_accounts()

    rece = find_acc(accounts)
    if rece is None:
        return

    acc_id = next(acc for acc, info in accounts.items() if info == rece)

    nic = rece['NIC']
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
                file.write(f"{acc_id}\t{nic}\t{a_name}\t{a_num}\t{amount}\tDeposit\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t\n")
            # Update accounts
            with open("accounts.txt", "w") as file:
                    for acc_id, details in accounts.items():
                        file.write(f"{acc_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
            break
        else:
            print("Negative or zero amount")
# Withdraw money from account         
def withdraw():
    accounts = load_accounts()
                    
    rece=find_acc(accounts)
    if rece is None:
        return

    acc_id = next(acc for acc, info in accounts.items() if info == rece)
    nic = rece['NIC']
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
            if rece['Opening_bal']<=5000:
                print("Warning: Balance below Rs. 5000!")
            # record transaction
            with open("transactions.txt", "a") as file:
                file.write(f"{acc_id}\t{nic}\t{a_name}\t{a_num}\t{amount}\tWithdraw\t{open_bal}\t{date.strftime("%Y-%m-%d-%H:%M:%S")}\t\n")
            # Update accounts
            with open("accounts.txt", "w") as file:
                    for acc_id, details in accounts.items():
                        file.write(f"{acc_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
            break
        else:
            print("Withdrawals greater than the balance")   
# Transfer money between accounts
def transfer_money(accounts):
    print("======== Money Transfer ========")
    try:
        sender_id = int(input("Enter Sender Account Number(Ex-1000): "))
        receiver_id = int(input("Enter Receiver Account Number(Ex-1000): "))
    except ValueError:
        print("Invalid input. Account numbers must be numeric.")
        return

    if sender_id not in accounts or receiver_id not in accounts:
        print("Sender or receiver account not found.")
        return

    sender = accounts[sender_id]
    receiver = accounts[receiver_id]

    sender_acc_id = sender_id
    receiver_acc_id = receiver_id

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
        file.write(f"{sender_acc_id}\t{sender['NIC']}\t{sender['Name']}\t{sender['Account_type']}\t{amount}\twithdraw\t{sender['Opening_bal']}\t{date}\n")
        file.write(f"{receiver_acc_id}\t{receiver['NIC']}\t{receiver['Name']}\t{receiver['Account_type']}\t{amount}\tdeposit\t{receiver['Opening_bal']}\t{date}\n")

    # Update accounts file
    with open("accounts.txt", "w") as file:
        for acc_id, details in accounts.items():
            file.write(f"{acc_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")
# Add monthly interest to all accounts
def add_interest(accounts):
    print("====== Add Interest to Accounts ======")
    while True:
        try:
            interest_rate=float(input("Enter Interest rate for current Month % :"))
            break
        except ValueError:
            ("Enter digits Only")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for acc_id, acc in accounts.items():
        acc_type = acc['Account_type']
        if acc_type in ['saving', 'fixed','current']:
            current_balance = acc['Opening_bal']
            interest = current_balance * (interest_rate/100)
            acc['Opening_bal'] += interest
            print(f"Interest of {interest:.2f} added to account {acc_id} {acc['Name']}")

            # recoard interest transaction
            with open("transactions.txt", "a") as file:
                file.write(f"{acc_id}\t{acc['NIC']}\t{acc['Name']}\t{acc['Account_type']}\t{interest:.2f}\tInterest\t{acc['Opening_bal']:.2f}\t{date}\n")


    with open("accounts.txt", "w") as file:
        for acc_id, details in accounts.items():
            file.write(f"{acc_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']:.2f}\t{details['Date']}\n")

# Check balance
def get_Bal(User_Acc,nic):
    if nic is None:
        nic = input("Enter NIC number to search accounts(Ex-2000123456): ").strip()
    matched_accounts = {acc_id: details for acc_id, details in User_Acc.items() if details['NIC'] == nic}

    if not matched_accounts:
        print("No accounts found for this NIC.")
        return None

    print("\nAccounts found:")
    print("Account No\tAccount Type\tCustomer Name\tBalance")
    for acc_id, details in matched_accounts.items():
        print(f"{acc_id}\t\t{details['Account_type']}\t\t{details['Name']}\t\t{details['Opening_bal']}")

    while True:
        try:
            seek_id = int(input("\nEnter the Account number to view its balance(Ex-1000): "))
            if seek_id in matched_accounts:
                selected = matched_accounts[seek_id]
                print("\nAccount Details:")
                print("NIC_Number        : Customer_name  : Acc_Type    : Balance        : Date")
                print('         '.join(str(value) for value in selected.values()))
                return selected
            else:
                print("Account number not found under this NIC.")
        except ValueError:
            print("Invalid input. Please enter a valid account number.")

#get nic to filter accounts
def get_nic_by_username(username):
    try:
        with open("user_nic_map.txt", "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2 and parts[0] == username:
                    return parts[1]
    except FileNotFoundError:
        print(f"{file} not found.")
    return None

# Show transaction history
def history(acc=None):
    print("Transaction History:\n")
    transactions = []

    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 8:
                    if acc is None or parts[0] == acc:
                        transactions.append(parts) 
    except FileNotFoundError:
        print("Transaction file not found.")
        return
    
    if acc:
        transactions = [t for t in transactions if t[0] == str(acc)]
        transactions[-5:]  # Get last 5 transactions

    headers = ["Account","NIC number","Customer_name", "Account_Type", "Transaction", "Status", "Close Balance", "Date"]
    
    if not transactions:
        print("No transactions found for this account.")
    elif len(transactions) < 5:
        print(f"Only {len(transactions)} transaction(s) found for this account:")
        print("{:<10} {:<20} {:<15} {:<15} {:<10} {:<10} {:<15} {:<30}".format(*headers))
        print("-" * 125)
        for trans in transactions:
            print("{:<10} {:<20} {:<15} {:<15} {:<10} {:<10} {:<15} {:<30}".format(*trans))
        print(f"Total transaction(s): {len(transactions)}")
    else:
        print("{:<10} {:<20} {:<15} {:<15} {:<10} {:<10} {:<15} {:<30}".format(*headers))
        print("-" * 125)
        i = 0
        for trans in transactions[-5:]:  # Last 5 transactions
            print("{:<10} {:<20} {:<15} {:<15} {:<10} {:<10} {:<15} {:<30}".format(*trans))
            i += 1
        print("Total (recent) transactions shown:", i)

def delete_customer(nic_to_delete):
    # Load all data
    customers = load_users()
    users = load_admins()
    accounts = load_accounts()

    # Load user_nic_map
    nic_map = {}
    try:
        with open("user_nic_map.txt", "r") as file:
            for line in file:
                username, nic = line.strip().split('\t')
                nic_map[username] = nic
    except FileNotFoundError:
        print("user_nic_map.txt not found.")
        return

    # Check if NIC exists
    if nic_to_delete not in customers:
        print("Customer not found.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete customer {nic_to_delete}? (Y/N): ").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return

    # Remove customer
    customers.pop(nic_to_delete)

    # Find and remove associated user from users and user_nic_map
    username_to_delete = None
    for username, nic in nic_map.items():
        if nic == nic_to_delete:
            username_to_delete = username
            break

    if username_to_delete:
        users.pop(username_to_delete, None)
        del nic_map[username_to_delete]

    # Find and remove all associated accounts
    acc_ids_to_delete = [acc_id for acc_id, details in accounts.items() if details['NIC'] == nic_to_delete]
    for acc_id in acc_ids_to_delete:
        del accounts[acc_id]

    # Filter out matching transactions
    transactions = []
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 1:
                    acc_id = parts[0]
                    if acc_id.isdigit() and int(acc_id) not in acc_ids_to_delete:
                        transactions.append(line.strip())
    except FileNotFoundError:
        print("transactions.txt not found.")

    # Save updated customers
    with open("customers.txt", "w") as file:
        for nic, details in customers.items():
            file.write(f"{nic}\t{details['name']}\t{details['phone_no']}\t{details['address']}\t{details['Date']}\n")

    # Save updated users
    with open("users.txt", "w") as file:
        for user, pwd in users.items():
            file.write(f"{user}\t{pwd}\n")

    # Save updated user_nic_map
    with open("user_nic_map.txt", "w") as file:
        for user, nic in nic_map.items():
            file.write(f"{user}\t{nic}\n")

    # Save updated accounts
    with open("accounts.txt", "w") as file:
        for acc_id, details in accounts.items():
            file.write(f"{acc_id}\t{details['NIC']}\t{details['Name']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\n")

    # Save updated transactions
    with open("transactions.txt", "w") as file:
        for line in transactions:
            file.write(line + "\n")

    print(f"Customer {nic_to_delete} and all related data have been deleted.")

def exit(): # Exit message
    
    print("Thank for using our service")

def display_total_users():

    try:
        with open("users.txt", "r") as file:
            i=0
            for line in file:
                i=i+1
            print("Total users:",i)
                    
    except FileNotFoundError:
        print("Transaction file not found.")

def display_customer_list():
    x=[]
    try:
        with open("customers.txt", "r") as file:
            for line in file:
                parts=line.strip().split('\t')
                if len(parts) == 5: 
                    acc_no = int(parts[0])
                    name = parts[1]
                    x.append(f"{acc_no} : {name}")
            print(x)           
    except FileNotFoundError:
        print("Transaction file not found.")

def display_customer_no():

    try:
        with open("customers.txt", "r") as file:
            i=0
            for line in file:
                i=i+1
            print("Total customers:",i)
                    
    except FileNotFoundError:
        print("Transaction file not found.")


def check_customers_without_accounts(customers, accounts):
    if not customers:
        print("No customers found.")
        return

    customer_nics = set(customers.keys())
    account_nics = {details['NIC'] for details in accounts.values()}

    no_account_nics = customer_nics - account_nics

    if not no_account_nics:
        print("All customers have at least one account.")
    else:
        print("\nCustomers without accounts:")
        print("NIC Number     : Name")
        for nic in no_account_nics:
            print(f"{nic:15}: {customers[nic]['name']}")

def display_account_no():

    try:
        with open("accounts.txt", "r") as file:
            i=0
            for line in file:
                i=i+1
            print("Total Accounts:",i)
                    
    except FileNotFoundError:
        print("Transaction file not found.")

def  show_current_date():
    time= datetime.datetime.now()
    print("Current date : ",time.strftime("%Y-%m-%d"))

def type_summary(acc):
    deposit_count = 0
    withdraw_count = 0

    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) >= 8 and parts[0] == acc:
                        transaction_type = parts[5]
                        if transaction_type == 'Deposit':
                            deposit_count += 1
                        elif transaction_type == 'Withdraw':
                            withdraw_count += 1
            print("Customer not found")
            print(f"  Deposits     : {deposit_count}")
            print(f"  Withdrawals  : {withdraw_count}")
    except FileNotFoundError:
        print("Transaction file not found.")
        return

def password_change():
    while True: 
        try:
            change_U=input("Enter user name to change password : ")
            break
        except ValueError:
            print("Invalid number. Please enter digits only.")

    admins=load_admins()
    
    if change_U in admins:
        print("User Found")
        x=admins[change_U]
    else:
        print("User not found.")

    while True: 
        try:
            psw=input("Enter password to change to change password : ")
            break
        except ValueError:
            print("Invalid characters. Please enter digits only.")

    admins[change_U]=psw
    y=admins[change_U]
    print("Your password has been updated")

    with open("users.txt", "w") as file:
        for user,password in admins.items():
            file.write(f"{user}\t{password}\t\n")




Attempt=3
i=0
while i<3:
    if not os.path.exists("users.txt"):
        with open("users.txt", "a") as file:
            admin_hash = hash_password("123")
            file.write(f"Admin\t{admin_hash}\n")  
    admins=load_admins()
    
    print("=========Login Menu=========")
    print("1.Admin")
    print("2.Customer")
    print("3.Log out")
    while True:
        try:
            pick=int(input("Choose an Option (1-3) : "))
            break
        except ValueError:
            print("Invalid number. Please enter correct number.")
    
    if pick==3:
        print("Logging out")
        break

    username = input("Enter Your User Name : ")
    password = input("Enter Your Password : ")
    hashed_input_password = hash_password(password)

    if pick==1: 
        if username in admins and admins[username] == hashed_input_password:
            print("Welcome",username,"(Admin)")
            while True:
                print("============Menu===========")    
                print("1.Create User")
                print("2.Search Customer")
                print("3.Create Account")
                print("4.Search Account")
                print("5.Deposit Money")
                print("6.Withdrw Money")
                print("7.Transfer Money")
                print("8.Add intrest")
                print("9.Check balance")
                print("10.Transaction Histry")
                print("11.Deactivation")
                print("12.Exit")
                print("13.Display Users")
                print("14.Display customer list")
                print("15.Display customer numbers")
                print("16.customer check")
                print("17.Account count")
                print("18.Show current date")
                print("19.transcation type summary")
                print("20.Change password")

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
                    transfer_money(accounts)
                
                elif select==8:
                    accounts = load_accounts()
                    add_interest(accounts)
                
                elif select==9:
                    accounts = load_accounts()
                    get_Bal(accounts,nic=None)

                elif select==10:
                    acc = input("Enter Account Number to view recent transactions (Ex-1000): ").strip()
                    if acc.isdigit():
                        history(acc)
                    else:
                        print("Invalid account number.")
                
                elif select==11:
                    nic = input("Enter the NIC number of the customer to delete (Ex-2000123456): ").strip()
                    delete_customer(nic)

                elif select==12:
                    exit()
                    break
                
                elif select==13:
                    display_total_users()

                elif select==14:
                    display_customer_list() 

                elif select==15:
                    display_customer_no() 
                
                elif select==16:
                    customers = load_users()
                    accounts = load_accounts()
                    check_customers_without_accounts(customers, accounts)

                elif select==17:
                    display_account_no()

                elif select==18:
                    show_current_date()
                
                elif select==19:
                    acc = input("Enter Account Number to view history(Ex-1000): ").strip()
                    type_summary(acc)
                
                elif select==20:
                    password_change()

        else:
            print("Customer not found.")
            Attempt=Attempt-1
            print("Attempt left " ,Attempt)

    elif pick==2:
        if username in admins and admins[username] == hashed_input_password:
            nic = get_nic_by_username(username)
            customers = load_users()
            if nic and nic in customers:
                name = customers[nic]['name']
                print(f"\nWelcome, {name} (Customer)")
                    
            while True:
                print("============Menu===========")    
                print("1.Create User")
                print("2.Deposit Money")
                print("3.Withdrw Money")
                print("4.Check balance")
                print("5.Transfer Money")
                print("6.Transaction History")
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
                    nic = get_nic_by_username(username)
                    final=get_Bal(accounts,nic)

                elif select==5:
                    accounts = load_accounts()
                    transfer_money(accounts)
                    
                elif select==6:
                    nic = get_nic_by_username(username)
                    if nic:
                        history(nic)
                    else:
                        print("Could not find NIC for this user.")

                elif select==7:
                    exit()
                    break
        else:
            print("Customer not found.")
            Attempt=Attempt-1
            print("Attempt left " ,Attempt)

    else:
        print("User name and Password are incorrect, Enter correctly")
        
    i=i+1
    if Attempt==0:
        print("Too many failed attempts.Exiting Program")