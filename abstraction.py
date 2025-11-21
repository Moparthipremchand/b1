class atmexample:
    def __init__(self, name, ac_number, pin, ac_balance):
        self.holdername=name 
        self.accountnumber=ac_number
        self.atmpin=pin 
        self.balance=ac_balance
     
    def __pincheck(self,incomingpin):
        return self.atmpin== incomingpin
     
    def __dposite_update_balance(self,incoming_amount):
        self.balance+=incoming_amount
        

    
    
    def deposite(self, accountpin, incoming_amount):
        if self.__pincheck(accountpin):
            self.__dposite_update_balance(incoming_amount)
            print(f"{incoming_amount} successfully deposited \n available balance :{self.balance}")
            
        else:
            print("you entere wrong pin")
            
    
    def __withdraw_update_balance(self,incoming_amount):
        self.balance-=incoming_amount
        
    
    def withdraw(self, accountpin, incoming_amount):
        if incoming_amount<=self.balance:
            if self.__pincheck(accountpin):
                self.__withdraw_update_balance(incoming_amount)
                print(f"{incoming_amount} successfully withdrawn \n available balance :{self.balance}")
            else:
                print("you entere wrong pin")
        else:
            print("insufficient fund")
                
        
    def checkbalance(self,accountpin):
        if self.__pincheck(accountpin):
            print(f"available balance {self.balance}")
        else:
            print("you entere wrong pin")
    
    
atm=atmexample("premchand", 9876543212345, 1989, 5000)


options=int(input("withdraw = 1 \n deposite = 2 \n check balance = 3 \n enter your option  :"))

if options ==2:
    amount=int(input("enter your ammount  :"))
    atmpin=int(input(" enter atm pin  :"))
    atm.deposite(atmpin,amount)

elif options ==1:
    amount=int(input("enter your ammount  :"))
    atmpin=int(input(" enter atm pin  :"))
    atm.withdraw(atmpin,amount)

elif options==3:
    atmpin=int(input(" enter atm pin  :"))
    atm.checkbalance(atmpin)
    
else:
    print("select only given option")