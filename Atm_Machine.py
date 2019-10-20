pin=input("Please enter yout ATM pin")
if (len(pin)==4):
    amt=int(input("Please enter your Amount:"))
    if (amt<10000 and amt>0):
        cvv=input("Please enter your CVV No:")
        if(len(cvv)==3):
            print("Transaction Successful")
        else :
            print("Transaction Failed")
    else:
        print("Insufficient Balance")
else:
    print ("please check your pin")
