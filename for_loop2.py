##print numbers from 1 to 10

for i in range(1,11):
    print(i)


##print only od numbers from 1 to 10
for i in range(1,11):
    if i % 2 == 0:
        print(i)



for i in range(0,11,2):
    print(i)


##print even numbers from 1 to 10
for i in range(1,11,2):
    print(i)

for i in range(1,11):
    if i % 2 != 0:
        print(i)


##print sum of odd numbers from 1 to 10
sum=0
for i in range(1,11):
    if i % 2 != 0:
        sum += i
print(sum)



sum_of_odd=0
for i in range(1,11,2):
    if i % 2 != 0:
        sum_of_odd += i
print(sum_of_odd)



##print sumof even numbers from 1 to 10
sum_of_even=0
for i in range(1,11):
    if i % 2 == 0:
        sum_of_even += i
print(sum_of_even)


##print sum of odd sum of even product of odd product of even
sum_of_numbers=0
sum_of_odd=0
sum_of_even=0
sum_of_even_product=1
sum_of_odd_product=1
for i in range(1,11):
    if i in range(1,11):
        sum_of_numbers += i
    if i % 2 == 0:
        sum_of_even += i
        sum_of_even_product *= i
    else:
        sum_of_odd += i
        sum_of_odd_product *= i
        
print("sum_of_numbers",sum_of_numbers)
print("sum_of_odd",sum_of_odd)
print("sum_of_even",sum_of_even)
print("sum_of_even_product",sum_of_even_product)
print("sum_of_odd_product",sum_of_odd_product)
        
        
##print sum of numbers from1 to 10       
sum_of_numbers=0
for i in range(1,11):
    sum_of_numbers += i
    print( sum_of_numbers)


total_sum = sum(range(1,11))
print(total_sum)

sum_of_numbers = 0
for i in range(1,11):
    sum_of_numbers += i
    print(sum_of_numbers,end=" ")
print(sum_of_numbers)

total_sum = sum(range(1,11))
print(total_sum)
        
        
##write a program to print numbers from 10 to 1
for i in range(11,0,-1):
    print(i)


##print only two digit numbers from list
numbers=[99,2,34,56,234,-2,-43,-456,-32,100,-234]
for i in numbers:
    if i >9 and i<100:
        print(i)
    elif i>-100 and i<-10:
        print(i)
    else:
        print("none")

numbers=[99,2,34,56,234,-2,-43,-456,-32,100,-234]
for i in numbers:
    if i > 9 and i < 100:
        print(i)



##print totla price in a cart
items_price=[100,20,40,30,10]
sumof=0
for i in items_price:
    sumof += i
print(sumof)