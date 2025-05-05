def Create_user(nic_no,name,ph_no,address):
    
    User1[nic_no]={
        'name' : name,
        'phone_num' : ph_no,
        'place'    : address
    }
    return User1

def find_user(Customer):
    seek_id=int(input("Enter user ID : "))
    if seek_id in Customer:
        print("User Found:", Customer[seek_id])
    else:
        print("User not found.")

def create_Account(nic_no,Acc_no,Acc_type,Intial_bal):

    User2[nic_no]={
        'Account_num' : Acc_no,
        'Account_type' : Acc_type,
        'Opening_bal' : Intial_bal
    }
    return User2
    return Intial_bal
   
def find_acc(User_Acc):
    seek_id=int(input("Enter user ID : "))
    if seek_id in User_Acc:
        print("User Found:", User_Acc[seek_id])
        dict_val=User_Acc[seek_id]
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
        print("2.Search Customer Details")
        print("3.Create Account")
        print("4.Search Account Details")
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
            #status="Active"
            Customer=Create_user(nic_no,name,ph_no,Address)
            #return(Customer)
            print("Your Profile has been Created")
        
        elif select==2:

            find_user(Customer)
        
        elif select==3:

            print("===========Account details===========")
            nic_no=int(input("Enter NIC no: "))
            Acc_no=int(input("Enter Account no: "))
            Acc_type=input("Enter Account Type:")
            Intial_bal=int(input("Enter Intial Balance:"))

            User_Acc=create_Account(nic_no,Acc_no,Acc_type,Intial_bal)
            print("Your Account has been Created with",Intial_bal)
            print(User_Acc)

        elif select==4:
            find_acc(User_Acc)

        elif select==5:
            rece=find_acc(User_Acc)
            open_bal=rece['Opening_bal']
            open_bal+=deposit()
            print("Balance updated with",open_bal)
            #a=dippo(User_Acc)
            rece['Opening_bal']=open_bal
            print(User_Acc)
        elif select==6:
            Intial_bal-=withdraw(Intial_bal)
            print("Balance updated with",Intial_bal)

        elif select==7:
            final=get_Bal(Intial_bal)
            print("This is your balance",final)

        elif select==8:
            history(Intial_bal,Intial_bal,Intial_bal,final)
            print("Your available balance is updated ")
 
        elif select==9:
            d=exit()
            break