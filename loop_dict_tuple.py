skils=["html","css","python"]
details = {
    "id":1,
    "name":"ravi",
    "sttream":"CSE",
    "year":4,
    "age":22,
    "college":"10k coders",
    "skils":skils
}
# print(details["skils"])
# print(details["sttream"])
for i in details.keys():
    print(i)
for i in details.values():
    print(i)
for i in details.items():
    print(i)
    
for i,j in details.items():
    print(i,j)

for i,j in details.items():
    print(i,":",j)
    
## palindrome

userinput=input("enter string")
if userinput[::-1]==userinput:
    print(userinput,": is palindrom")
else:
    print(userinput,": is not palindrom")


user=""
userinput=input("enter word  :")
for i in range(len(userinput)-1,-1,-1):
    print(userinput[i])
    user+=userinput[i]
print(user)
if user==userinput:
    print(userinput,"is palindrom")
else:
    print(userinput,"is not palindrom")
    

## marks grade

marks={"vamsi":88, "ramu":72,"vikram":56,"nandhana":67,"bob":98,"ajay":40}
for i in marks:
    print(i)
    print(marks[i])
    if marks[i]>92:
        print("A+ grade",marks[i],i)
    elif marks[i]>70 and marks[i]<=92:
        print("B+ grade",marks[i],i)
    elif marks[i]>50 and marks[i]<=70:
        print("C+ grade",marks[i],i)
    else:
        print("fail",marks[i],i)
        
        
obj={
    "id":1,
    "name":"vikaranth",
    "job":True,
    "sibling":True,
    "ismarried":True,
    "isbike":True,
    "height":5.9,
    "list":[1,2,3,4]
}
new={}
new1={}
for i in obj:
    if type(obj[i])==int:
        new[i]=obj[i]
    if type(obj[i])==bool:
        new1[i]=obj[i]
print(new)
print(new1)



# heighest salery in dict key value pair in python simple program
salaries = {
    "Rahul": 45000,
    "Sneha": 52000,
    "Amit": 60000,
    "Priya": 58000
}

highest = max(salaries, key=salaries.get)
print("Highest salary is:", salaries[highest], "earned by", highest)



#occurence of letter in a dictounery
text = "banana"
count_dict = {}

for ch in text:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print(count_dict)


# list of dicts get only items which are only belongs to electronics and find total items count
items = [
    {"name": "Laptop", "category": "electronics"},
    {"name": "Shirt", "category": "clothing"},
    {"name": "Mobile", "category": "electronics"},
    {"name": "Book", "category": "stationary"},
    {"name": "Headphones", "category": "electronics"}
]

electronics = [item for item in items if item["category"] == "electronics"]


count = len(electronics)

print("Electronics items:", electronics)
print("Total electronics count:", count)



#prime numbers
user=int(input("enter number  :"))
for i in range(2,user):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



