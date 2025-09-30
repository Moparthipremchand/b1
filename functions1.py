##1. creat ea variable x and assign the value 10 to it. and print x
x=10
print(x)


##2.create two varablies: a = 5, b = 3.2. print  their sum and checkthe type of each

a=5
b=3.2
c=a+b
print(c)
print(type(c))


##3.Store your name in a variable my_name and print it.

name="premchand"
print(name)

##4.Create a variable is_student and assign it the value True . Print the variable and its type.


is_student=True
print(type(is_student))


##5.Convert the integer 100 into a string and print the result with its type.
int=100
string=str(int)
print(string)
print(type(string))

##6.Take a string "45" and convert it into an integer. Add 5 and print the result.

str="45"
integer=int(str)
print(integer)
print(integer+5)


##7.Create a variable temperature and assign a float value. Convert it to integer and print

x=50
varable=x
float_value=float(x)
print(float_value)
print(type(float_value))
integer=int(float_value)
print(integer)


##8.Write a program to input your age and print a message like: "You are 25 years old."

age=int(input("enter you age"))
print(f"you are {age} years old")

##9.Concatenate two strings: "Hello" and "Python" and print the result


string1="hello "
string2=" python"
print(string1+string2)


##10.Check and print the type of each: 23 , "hello" , 3.14 , True

print(f"{type(23)},{type("hellow")},{type(3.14)},{type(True)}")
types=[23, "hellow", 3.14, True]
for i in types:
    print(type(i))


##11.Create a list of 5 fruits and print the list.

fruits=["apple","graphs","banana","mango","oranges"]
##print(fruits)
for i in fruits:
    print


##12.Create a tuple of 3 numbers and print the second item.
tuples=("ravi","ram","vikarant")
print(tuples[1])


##13.Create a list of 5 numbers. Replace the third number with a new value and printthe list.
numbers=["vikranth","ramana","jayanth","vijay","harish"]
numbers.append("ram")
numbers[3]="ram"
print(numbers)



num=[1,2,3,4,5,6]
print(num)
num[2]=45
print(num)


##14.Create a dictionary with keys: name , age , city . Assign your own values and print the dictionary.


details={
    "name":"vijay",
    "age":23,
    "city":"guntur"
}

print(details)


##15.From the above dictionary, print only the value of the city 
details={
    "name":"vijay",
    "age":23,
    "city":"guntur"
}
print(details["city"])

##16.Add a new key gender to the existing dictionary and print it.

details={
    "name":"vijay",
    "age":23,
    "city":"guntur"
}

details["gender"]="male"
print(details)


##17.Create a list of numbers and print only the even numbers using a loop.
numbers=[1,2,3,4,5,6,7,8,9,0]
for i in numbers:
    if i%2==0:
        print(i)


##18Convert a tuple (1, 2, 3) to a list and add a new item to it
tuples=(1,2,3,4,5,6,7,8)
lists=[tuples]
lists.append(88)
print(lists)



tuples=(1,2,3,4,5,6,7,8)
lists=list(tuples)
lists.append(88)
lists[3]=88
print(lists)

##19.Create two sets: {1,2,3} and {3,4,5} . Find and print their intersection.
set1={1,2,3}
set2={3,4,5}
result=set1.intersection(set2)
print(result)


setof1={2,0,3,4,5,6,7}
setof2={0,9,8,7,6,5,}
common=setof1.intersection(setof2)
print(common)


##20.Create a dictionary of 3 students and their marks. Print each student's name withtheir marks.

marks={
    "student1":45,
    "student2":55,
    "student3":65,
}
for i,j in marks.items():
    print(i,j)


marks={
    "student1":45,
    "student2":55,
    "student3":65,
}

marks["student4"]=75
print(marks)



##21wap to find pNumbers in certain range?
number=int(input("enter number   :"))
for i in range(2,number+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        
        
        
##22##wap to find pNumbers in list? andc reate new list?
p_list = [2,3,4,5,6,7,8,9,11,13,1,4,15,19]
n_list = []
for i in p_list:
    if i > 1:   
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            n_list.append(i)
print("Prime numbers list:", n_list)



##write a program to print given number is prime or not
number=int(input("enter a number   :"))
factor_count=0
for i in range(1,number):
    if number%i==0:
        factor_count+=1
if factor_count==2:
    print(f"{number} is priem number having only two factors")
else:
    print(f"{number} is not prie number because {number} having more than two factors")