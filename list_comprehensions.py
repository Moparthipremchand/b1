n = 30
result = [print(msg) for msg in ([f"{n} is prime"] if n >= 2 and len([i for i in range(1, n+1) if n % i == 0]) == 2 else ["not a prime"] if n < 2 else [f"{n} is not prime"])]
print(result)


n=5
res=print("prime") if n>=2 and len([i for i in range(1,n+1) if n % i ==0 ] ) ==2 else print("not prime")
print(res)


nums=[1,2,3,4,5,6,7,8,9,10]
numbers=[i for i in nums]
print(numbers)

a=[11,23,12,15,66,45,78,34,23,98,90,77,45,25]
even_numbers=[k for k in a if k%2==0]
print(even_numbers)

## square of numbers
numbers=[1,2,3,4,5,6,7]
square=[i**2 for i in numbers]
print(square)

a=["p","r","e","m","c","h","a","n","d"]
## result=[i*"123" for i in a] string not concate with string(string not multple wit string)
result=[i+"123" for i in a]
print(result)

c=[True, False, "prem"]
response=[i for i in c if type(i)==str]
print(response)


b=[10,20,30,2,45,67,43]
res=[i for i in b if i%2==0]
print(res)

d=[True, False, "prem", 10,20,30,2,45,67,43, "345", "786"]
res=[i for i in d if type(i)==str and i.isdigit()]
print(res)

e="lear from without mistake "
res=[i for i in e]
print(res)

e="premchand"
vowel="aeiouAEIOU"
res=[i for i in e if i not in vowel]
print(res)

f="vamsi is a triner in hyd"
vowel="aeiouAEIOU"
space=" "
res=[i for i in f if i not in vowel if i not in space]
print(res)


## task
f="vamsi is a triner in hyd"
vowel="aeiouAEIOU"
space=" "
res="".join([i for i in f if i not in vowel])
print(res)


for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            
            break
    else:
        print(i, end=" ")
        
prime=[i for i in range(2, 100) if all(i % j != 0 for j in range(2, i))]
print(prime)

n=22
res=[print("its prime")] if n>=2 and len([i for i in range(1,n+1) if n%i==0]) ==2 else print("not prime")