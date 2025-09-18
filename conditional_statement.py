## 1. Check if a number is positive, negative, or zero
user=int(input("enter number  :"))
if user > 0:
    print(user," is positive number")
elif user < 0:
    print(user, " is negative number")
    
else:
    print(user, "is equal to zero")


##2 Find the largest among three numbers
num1=int(input("enter number1   :"))
num2=int(input("enter number2   :"))
num3=int(input("enter number3   :"))
if num1 > num2 and num1 > num3:
    print("Number1 is the largest:", num1)

elif num2 > num1 and num2 > num3:
    print("Number2 is the largest:", num2)

elif num3 > num1 and num3 > num2:
    print("Number3 is the largest:", num3)

elif num1 == num2 and num1 > num3:
    print("Number1 and Number2 are equal and largest:", num1)

elif num1 == num3 and num1 > num2:
    print("Number1 and Number3 are equal and largest:", num1)

elif num2 == num3 and num2 > num1:
    print("Number2 and Number3 are equal and largest:", num2)

else:
    print("All three numbers are equal.")
print(max(num1,num2,num3),"is maximum number")


## Check if a character is a vowel
user=(input("enter only one alphabetes"))
vowel="aeiouAEIOU"
if user in vowel:
    print(user,"is vowel")
else:
    print(user," is not in vowel")



## Check whether a number is even and divisible by 5
number=int(input("enter number"))
if number%5==0 and number%2!=0:
    print(number,"is devisible by 5")
    
else:
    print(number,"is not devisible by 5")



##Electricity Bill Calculato
units=int(input("enter units "))
if units <= 100:
    print("current bill",units*5)
elif units > 100 and units <= 200:
    print("current bill is",units*7)
elif units > 200:
    print("current bill is",units*10)
else:
    print(None) 



## Student Grade Calculation
student=int(input("enter marks"))
if student >=90:
    print("A grade")
elif student < 90 and student > 75:
    print("B grade")
else:
    print("C grade")
    
    

##7. Check Login Credentials
user=input("enter user name")
password=int(input("enter password"))
user_name="premchand"
user_password=1234
if user == user_name and password == user_password:
    print("login successfully")
else:
    print("you entred wrong credentials ")



## Take two numbers and an operator (+, -, *, /) and print the result.
number1=int(input("enter number 1  :"))
number2=int(input("enter number 2  :"))
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)


##. Check if number is in a list
my_list=[2,3,4,5,6,7,8,9]
user=int(input("enter number  :"))
if user in my_list:
    print(user,"in my_list")
else:
    print(user,"not in my_list")



##Check if a string is a palindrome
string=input("enter string   :")
if string== string[::-1]:
    print(string,":  is palindrom")
else:
    print(string,":  not palindrom")


## Check if a number is within a range
start_r=10
end_r=50
user=int(input("enter number  :"))
if user >=10 and user <= 50:
    print("user in range between",start_r,"and", end_r)
else:
    print("user not-in range between",start_r,"and", end_r)


##  Determine age group
##  Task:
##  Categorize age into: - <13 → Child- 
##  13–19 → Teen- 
##  20–59 → Adult- 
##  60+ → Senior
age=int(input("enter age   :"))
if age <=12:
    print(" is chaild")
elif age >13 and age <=19:
    print("is teenager")
elif age >=20 and age <=59:
    print("is adult")  
else:
    print("is senior cityzen")


##  Compare two strings ignoring case
##  Task:
##  Check if two strings are equal (case-insensitive)
string1=input("enter string      :")
string2=input("enter string      :")
n=string1.lower()
m=string2.lower()
if n == m:
    print(" bothstrings are same")  
else:
    print("no same")


##  Traffic Light Simulator
##  Task:
##  Given a signal color (red , yellow , or green ), print appropriate action
colors=input("enter colors of this [red, yellow, green]")
if colors.lower() == "red":
    print("please stop")
elif colors.lower() == "yellow":
    print("you wil be ready to go in 10 sec")
elif colors.lower() == "green":
    print("go")
else:
    print("plese enter red or green or yellow")


##  ATM Withdrawal Simulation
##  Task:
##  Check if the entered withdrawal amount is a multiple of 100 and within the available balance.
account_balance=500000
withdraw_amout=int(input("enter amount   :"))
if withdraw_amout <= account_balance and withdraw_amout % 100 ==0 :
    if withdraw_amout <= 20000:
        print("withdraw success")
    else:
        print("enter amount less than 20000")
    # print("withdraw success")
elif withdraw_amout > account_balance:
    print("you entred more thans funds in your account")
else:
    print("please enter 100s only")
