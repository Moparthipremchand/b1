##  Question 1: Name Vowels from Long Names
##  Task: - List of 5 people - Check names with length > 5 - Extract vowels from those names - Store vowels in a
##  new list

mylist=["ajay", "ramu", "vikranth", "anu", "laptops"]
vowels="aeiouAEIOU"
new_list=[]
for i in mylist:
    if len(i) >=5:
        for j in i:
            if j in vowels:
                new_list.append(j)
                new_list.append(i)
print(new_list)


## 🔹 Question 2: Vowels from Odd Index in Sentence
##  Task: - Given a sentence - Pick characters at odd indices only - From those, extract vowels - Concatenate
##  those vowels and find length


sentence = input("enter a sentence    :")
vowel = "aeiouAEIOU"
vowel_list = []

for i in range(len(sentence)):
    if i % 2 != 0:  
        if sentence[i] in vowel:
            vowel_list.append(sentence[i])

print("Vowels at odd indices:", vowel_list)
print("Length:", len(vowel_list))


# 🔹 Question 3: Concat Strings & Find Length from List
#  Task: - List with mixed items - Extract only strings - Concatenate all strings - Print total length of final string


string=[2, "ramana",76.89, "arjun",True, "age", "andhrapradesh"]
for i in string:
    if type(i)==str:
        print(i)
        print(len(i))
        
        
        
        
# 🔹 Question 4: Extract 2-Digit Numbers from List
#  Task: - List with mixed data types (int, str, etc.) - Extract only numbers that are 2-digit (10 to 99) - Include
#  both integer and numeric strings - Push them into a new list and print it

o_list=[23,2,"string", True, 23, 4567, 90, "false, False","it"]
n_list=[]
for i in o_list:
    if type(i)==int:
        if i >10 and i<100:
            n_list.append(i)
print(n_list)