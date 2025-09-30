## write a program to iterate a number and print every digit in the number using while loop
n=int(input("enter number    :"))
while n>0:
    product=n%10
    print(product)
    n=n//10
    
    
# #write a program to print a reversed number using wile loop
number=int(input("enter numberr  :"))
reversed_number=0
while number> 0:
    digit=number%10
    reversed_number=reversed_number *10 +digit
    number=number//10
print(reversed_number)




##write a program to reverse a number digt ends with zero
number=int(input("entera number   :"))
n=str(number)
i=len(n)-1
reverse=""
while i >=0:
    reverse+=n[i]
    i-=1
print(reverse)



##write a program to reverse a string in whileloop
number=input("entera number   :")
i=len(number)-1
reverse=""
while i >=0:
    reverse+=number[i]
    i-=1
print(reverse)



## write a program to print sum of digits in a number using while loop
number=int(input("enter a number   :"))
t_sum=0
while number>0:
    digit=number%10
    t_sum+=digit
    number=number//10
print(t_sum)



## write aprogram to prit how many digits in a number
number=int(input("enter a number   :"))
count=0
while number>0:
    count+=1
    number=number//10
print(count)





## write aprogram to prit how many digits in a number
number=int(input("enter a number   :"))
count=0
while number>0:
    count+=1
    number=number//10
print(count)



##write a program to print sum of digit n a number until it comes to single digit
number = int(input("Enter a number: "))
while number >= 10: 
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    number = sum_digits
print("Single digit sum:", number)