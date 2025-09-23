##print all vowels from list of single charactor

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
vowels="aeiouAEIOU"
for i in alpha:
    if i in "aeiouAEIOU":
        print(i)
        
## print all str whic are len > 5 and push to new list
names=["vikranth", "ajay", "muragun", "nandha", "may", "jun"]
empty=[]
for i in names:
    if len(i) >5:
        empty.append(i)
print(empty)




##print all odd indecies values in list
a=[1,2,3,4,5,6,7,8,9]
for i in range(1,len(a),2):
    print(i)
    
    
    
    
##print all odd indices values and find only str and that too len > 3 and len<5
b=[1,3,"sankar","ravi", "prem","mokashitha", "ramu", "sar"]
for i in range(1,len(b),2):
    if type(b[i])==str:
        if len(b[i])>=3 and len(b[i])<=5:
            print(b[i])
            
            
            
            
##print all even indices values from list and push to new list

lis=[1,3,"sankar","ravi", "prem","mokashitha", "ramu", "sar"]
new_lis=[]
for i in range(1,len(lis),2):
    new_lis.append(lis[i])
print(new_lis)