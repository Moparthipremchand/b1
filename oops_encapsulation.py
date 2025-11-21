# class atmcard:
#     def __init__(self,n,num,p,c):
#         self.name=n
#         self._accoutnumber=num
#         self.__pin=p
#         self.__cvv=c
        
#     def setpin(self,np):
#         self.__pin=np
#         print(self.__pin,"updated")
    
# obj=atmcard("premchand",987654321,4567,423)
# print(obj.name)
# print(obj._accoutnumber)
# print(obj._atmcard__pin,"oldpin")
# print(obj._atmcard__cvv)

# obj.setpin(987)




class bank():
    def __init__(self,pn,acnum,b,pin):
        self.name=pn 
        self._account_number=acnum
        self.balance=b
        self.__atmpin=pin
        
    def checkbalance(self,atmpin):
        if self.__atmpin==atmpin:
            print(f"account holder : {self.name} \n available balace {self.balance}")
            
        else:
            print("enter correct pin to show details")   
            
            
    def withdraw(self,enterpin,withd):
        if enterpin == self.__atmpin:
            if withd %100==0:
                if withd <=self.balance:
                    print(f"{withd} successfully creited \n available balance {self.balance - withd}")
                else:
                    print("your accout have insufficient funds")
            else:
                print("enter only 100 or 200 or 500")
                
        else:
            print("enter correct pin")
                
                
        
    def deposite(self,acno,damount):
        if acno ==self._account_number:
            if damount > 100 and damount % 100==0:
                print(f"{damount} successfully deposited \n available balance : {self.balance + damount}")
            else:
                print("amount more than 100 and deposite only 100 200 500")
        else:
            print("enter account number correctly")
    
        
        
obj=bank("premchand",98765432123,5000,2348)
opt=int(input(" check balancee  :1 \n for withdraw  :2 \n deposite  :3 \n"))
if opt==1:
    atmpin=int(input(" enter your atm pin  :"))
    obj.checkbalance(atmpin)


elif opt==2:
    withd=int(input("enter ammount to withdraw  :"))
    enterpin=int(input("enter your pin :"))
    obj.withdraw(enterpin,withd)
        
elif opt==3:     
    acno=int(input("enter your account number  :"))
    damount=int(input("enter ammount  :"))
    obj.deposite(acno,damount )
else:
    print("choose given options only")