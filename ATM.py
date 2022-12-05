username='Dileep'
password='Msdhoni@07'

c_name=input("Enter Your name:")
c_pass=input("enter your password:")
if c_name==username and c_pass==password:
    print('''
    1.Deposite
    2.Withdraw
    3.Ministatement
    4.exit
    ''')
    ammount=50000
    option=int(input("select your option:"))
    if option==1:
        dep=int(input("Enter The Ammount:"))
        ammount+=dep
        print("Total ammount:",ammount)
    elif option==2:
        Withd=int(input("Enter the ammount:"))
        ammount-=Withd
        print("Total Ammount:",ammount)
    elif option==3:
        print("====ATM=======")
        print("UserName:",username)
        print("Total Ammount",ammount)
        print("thanks for visiting have a Great Day")
        print("====================================")
    elif option==4:
        exit()
else:
    print("please enter Correct Username and Pssword")