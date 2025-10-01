##write a function to print all yr family members  yr f_name,yr m_name, yr_sibiling_name in a print statement?
def family():
    f_name="MSR"
    m_name="MS"
    b_name="MAK"
    my_name="MPC"
    print(f"father name  :{f_name},  mother name  :{f_name},  brother name   :{b_name},   and my name   :{my_name}")
    
family()



# #write a function to print all yr  details like name,age,college,yearofpassedout,percentage,nativeplace  in a print statement?
def details():
    age=23
    name="MPC"
    city="guntur"
    college="vkdc"
    sports="shuttle"
    print(f"name is {name} and his age is {age}  from  {city} studed in {college} and his faverouit sport is {sports}")
    
details()


# #write a function which takes 2 args (1,11) and use for loop in function and print even numbers ?
x=int(input("enter number 1  :"))
y=int(input("enter number 2  :"))
def operators(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a/b)
    print(a**b)
    
operators(x,y)



##Write a function to print statements based on the matched criteria and conditions are youtube video quality selection 
quality=int(input("select video quality like (240p, 480p, 720p, 1080,4k)     :"))
def matched():
    if quality==240:
        print("video playing with quality 240p")
    elif quality==480:
        print("video playing with quality 480p")
    elif quality==720:
        print("video playing with quality 1080p")
    elif quality==4:
        print("video playing with quality 4k")
    else:
        print("select on;y available qualitys")
        
matched()





# #Write a function which needs to call 2 functions inside main function and main function is atm And Another 2 functions are withdraw and deposit functions and you can withdraw r deposit after entering crct pin only
pin = 65432
ac_balance = 50000

def atm(upin):
    if upin == pin:
        print("Your account balance is:", ac_balance)
    else:
        print("You entered wrong pin")

def withdraw(upin):
    global ac_balance
    if upin == pin:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= ac_balance:
            ac_balance -= amount
            print("Withdrawal successful!")
            print("Remaining balance:", ac_balance)
        else:
            print("Insufficient funds")
    else:
        print("You entered wrong pin")

def function():
    selection = input("Select 'withdraw' or 'atm': ").lower()
    upin = int(input("Enter your pin: "))

    if selection == "atm":
        atm(upin)
    elif selection == "withdraw":
        withdraw(upin)
    else:
        print("Invalid selection")

# Run
function()


