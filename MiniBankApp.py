
import datetime
def Create_user(nic_no,name,ph_no,address,date):
    
    User1[nic_no]={

        'name' : name,
        'phone_num' : ph_no,
        'place'    : address,
        'Date': date.strftime("%Y-%m-%d- %H:%M:%S")
    }
    return User1

def find_user(Customer):
    
    seek_id=int(input("Enter user ID : "))
    if seek_id in Customer:
        print("User Found:")
        x=Customer[seek_id]
        print("Customer_name  : Pho_number    : Address        : Date           :")
        print('         '.join(str(value)for value in x.values())) 
        
    else:
        print("User not found.")

def create_Account(nic_no,Acc_no,Acc_type,Intial_bal,date):

    User2[nic_no]={
        'Account_num' : Acc_no,
        'Account_type' : Acc_type,
        'Opening_bal' : Intial_bal,
        'Date'      : date.strftime("%Y-%m-%d- %H:%M:%S")
    }
    return User2
    return Intial_bal
   
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

def get_Bal(new2):
    return new2

def history(Int_bal,deposit,withdraw,final):
    
    x=In_bal
    y=deposit
    z=withdraw
    p=final

    print(f"Your Intial balance is :",x,"Deposited money :" ,y,"Withdraw Money :",z
    ,"Closing balance :",p)
 
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
            
            print("============User details============")
            nic_no=int(input("Enter NIC no:"))
            name=input("Enter user name:")
            ph_no=int(input("Enter user contact no:"))
            Address=input("Enter user resident area:")
            date=datetime.datetime.now()
            Customer=Create_user(nic_no,name,ph_no,Address,date)
            print("Your Profile has been Created")
            
            print("User_Id         : Customer_name : Pho_number    : Address       : Date                     :")
            for user_id,details in Customer.items():
                
                print(":",user_id," " *(12-len(str(user_id))),
                ":",details['name']," " *(12-len(details['name'])),
                ":",details['phone_num']," " *(12-len(str(details['phone_num']))),
                ":",details['place']," " *(12-len(details['place'])),
                ":",details['Date']," " *(18-len(str(details['Date']))),)

                file = open("customers.txt",'a')
                file.write(f"{user_id}\t{details['name']}\t{details['phone_num']}\t{details['place']}\t{details['Date']}\t")
                file.close

        elif select==2:
        

            find_user(Customer)
        
        elif select==3:

            print("===========Account details===========")
            nic_no=int(input("Enter NIC no: "))
            Acc_no=int(input("Enter Account no: "))
            Acc_type=input("Enter Account Type:")
            Intial_bal=float(input("Enter Intial Balance:"))
            date=datetime.datetime.now()
            User_Acc=create_Account(nic_no,Acc_no,Acc_type,Intial_bal,date)
            print("Your Account has been Created with",Intial_bal)
            
            print("User_Id         : Customer_name : Pho_number    : Address       : Date                     :")
            for user_id,details in User_Acc.items():
                
                print(":",user_id," " *(12-len(str(user_id))),
                ":",details['Account_num']," " *(12-len(str(details['Account_num']))),
                ":",details['Account_type']," " *(12-len(details['Account_type'])),
                ":",details['Opening_bal']," " *(12-len(str(details['Opening_bal']))),
                ":",details['Date']," " *(18-len(str(details['Date']))),)

                file = open("accounts.txt",'a')
                file.write(f"{user_id}\t{details['Account_num']}\t{details['Account_type']}\t{details['Opening_bal']}\t{details['Date']}\t")
                file.close

        elif select==4:
            find_acc(User_Acc)

        elif select==5:
            rece=find_acc(User_Acc)
            open_bal=rece['Opening_bal']
            open_bal+=deposit()
            print("Balance updated with",open_bal)
            rece['Opening_bal']=open_bal
            print(User_Acc)
            date=datetime.datetime.now()
            
            file = open("transaction.txt",'a')
            file.write(f"{user_id}\t{details['Account_num']}\t{rece}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t")
            file.close
            
        elif select==6:
            rece1=find_acc(User_Acc)
            open_bal=rece1['Opening_bal']
            open_bal-=withdraw(open_bal)
            print("Balance updated with",open_bal)
            rece1['Opening_bal']=open_bal
            print(User_Acc)

            file = open("transaction.txt",'a')
            file.write(f"{user_id}\t{details['Account_num']}\t{rece1}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t")
            file.close
            
        elif select==7:
            final=get_Bal(open_bal)
            print("This is your balance",final)

        elif select==8:
            #history(name,Address,status,Acc_no,Acc_type,Balance)
            file = open("customers.txt",'r')
            file = open("accounts.txt",'r')
            file = open("transaction.txt",'r')
            file.write(f"{user_id}\t{details['Account_num']}\t{rece1}\t{open_bal}\t{date.strftime("%Y-%m-%d- %H:%M:%S")}\t")
            file.close
            print("Your available balance is updated ")

        elif select==9:
            d=exit()
            break

# elif user==Us_name and pass_w==Pa_word:

#     while True:
#         print("============Menu===========")    
#         print("1.Create User")
#         print("2.Personal Details")
#         print("3.Search my Account")
#         print("4.Deposit Money")
#         print("5.Withdrw Money")
#         print("6.Check balance")
#         print("7.Transaction Histry")
#         print("8.Exit")
        
#         select=int(input("Choose an Option :"))
        
#         if select==1:
            
#             print("============User details============")
#             nic_no=int(input("Enter NIC no:"))
#             name=input("Enter user name:")
#             ph_no=int(input("Enter user contact no:"))
#             Address=input("Enter user resident area:")

#             Customer=Create_user(nic_no,name,ph_no,Address)
#             print(Customer)
#             print("Your Profile has been Created")
        
#         elif select==2:

#             find_user(Customer)

#         elif select==3:
#             find_acc(User_Acc)

#         elif select==4:
#             Cus_acc=int(input("Enter your Account No:"))
            
#             Intial_bal+=deposit()
#             print("Balance updated with",Intial_bal)
            
#         elif select==5:
#             Intial_bal-=withdraw(Intial_bal)
#             print("Balance updated with",Intial_bal)

#         elif select==6:
#             final=get_Bal(Intial_bal)
#             print("This is your balance",final)

#         elif select==7:
#             history(Intial_bal,Intial_bal,Intial_bal,final)
#             print("Your available balance is updated ")
 
#         elif select==8:
#             d=exit()
#             break

# else:    
#     print("Enter Correct User Name and password")
        
