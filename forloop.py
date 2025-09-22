##1. Print each character of a string.
user=input("enter any name   :")
for i in user:
    print(i)
    
    
##2. Print all even numbers from a list.

my_list=[1,2,3,4,5,6,7,8,9]
for i in my_list:
    if i%2==0:
        print(i)
        
        
        
##3. Calculate the sum of numbers in a tuple.

a=(2,3,4,5,6,7)
total=0
for i in a:
    print(total)
    total+=i
    
    
    
    
##4. Print names from a list of strings.

names=["ramu",True, 76, "vikram", 70.89]
for i in names:
    if type(i)==str:
        print(i)
        
        
        
##5. Print square of numbers using range.

number=int(input("enter number  :"))
for i in range(1,number+1):
    print(i**2)
    
    
    
    
##6. Count vowels in a string.


word=input("enter word")
vowels="aeiouAEIOU"
count=0
for i in word:
    if i in vowels:
        count+=1
        
print("vowels count", count)





##7. Reverse a string using for loop.

string=input("enter a string   :")
# for i in string:
print(string[::-1])




##8. Check if elements in list are positive.

elements=[2,3,"abcd",True,False, 4.6, None, -2,-5.7]
for i in elements:
    if i==True:
        print(i,":  is positive")
    else:
        print(i,":  is negative")
        
        
        
        
        
##9. Print odd-indexed characters in a string.

string=input("enter a strin   :g")
for i in  range(len(string)):
    if i%2!=0:
        print(string[i])
        
        
        
        
        
##10. Print multiples of 3 using range.

number=int(input("enter number   :"))
for i in range(1,number+1):
    if i%3==0:
        print(i)
        
        
        
        
##11. Find the product of numbers in a list.

list_num=[2,3,4,5,6,7,8,9]
product=0
for i in list_num:
    print(product)
    product+=i
    
    
    
    
    
##12. Count how many times a specific character appears in a string.

string=input("enter a string   :")
for i in set(string):
    print(i,string.count(i))
    
    
    
    
##13. Print each element of a tuple with its index.


elements=(2,4,6,"ram", "vkram", True, "age", False, 65.9, None)
for i in range(len(elements)):
    print(i,elements[i])
    
    
    
    
##14. Print numbers from 10 to 1 using range.

numbers=int(input("enter number    :"))
for i in range(numbers, 0,-1):
    print(i)
    
    
    
    
    
    
##15. Convert each string in a list to uppercase.

strings=["vikram", "jathin", "age", "nAME", "javanth"]
for i in strings:
    print(i.upper())