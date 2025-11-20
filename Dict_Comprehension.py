a="premchand"
res1=[i for i in a]
print(res1)

b="premchand"
res2=[print(i) for i in b]


c="premchand"
res3=[i for i in c if i in "AEIOUaeiou"]
print(res3)



d=["premchand",20, 20,56.98,True,False]
res4=[i for i in d if type(i)==str]
print(res4)


e=["premchand",20, 20,56.98,True,False]
res5=[i for i in e if type(i)==str or type(i)==bool]
print(res5)

f={"name":"premchand","age":23, "location":"nrt"}
res6=[i for i in f ]
print(res6)



f={"name":"premchand","age":23, "location":"nrt"}
res7=[f[i] for i in f ]
print(res7)


f={"name":"premchand","age":23, "location":"nrt"}
res8=[(f[i],i) for i in f ]
print(res8)


g=(1,2,3,4,5,6,True,"ram")
res9=[i for i in g ]
print(res9)




def even_number(even_num):
    print(even_num, end=" ")
    
h=[1,2,3,4,5,6,7,8,9,]
res10=[even_number(i) for i in h if i%2==0]



def odd_number(odd_num):
    print(odd_num, end=" ")
    
i=[1,2,3,4,5,6,7,8,9,]
res11=[odd_number(i) for i in h if i%2==1]



def odd_number_square(odd_num):
    print(odd_num, end=" ")
    
j=[1,2,3,4,5,6,7,8,9,]
res12=[odd_number_square(i**2) for i in h if i%2==1]


def even_number_square(even_num):
    print(even_num, end=" ")
    
k=[1,2,3,4,5,6,7,8,9,]
res13=[even_number_square(i**2) for i in h if i%2==0]





#    #  dict-comprehension

l="premchand"
res14={i:i for i in l}
print(res14)


m="premchand"
res15={i:i for i in m if i in "AEIOUaeiou"}
print(res15)


n="premchand"
res16={i:i for i in n if i not in "AEIOUaeiou"}
print(res16)

o="premchand"
res17={i:ord(i) for i in o}
print(res17)



p="premchand"
res18={i:ord(i) for i in p if i not in "AEIOUaeiou"}
print(res18)


q=[1,2,3,4,5,6,7,8,9]
res19={i:i+2 for i in q}
print(res19)



r=[1,2,3,4,5,6,7,8,9]
res20={i:i**2 for i in r}
print(res20)

s={"name":"premchand","age":23, "location":"nrt"}
res21={i:s[i] for i in s}
print(res21)



t=(1,2,3,4,5,6,True,"ram",False)
res22={i:t[i] for i in t if type(i)==bool}
print(res22)



u={"name1":"premchand","nzame2":"aravindu"}
res23={j for i in u for j in u[i]}
print(res23)



u={"name1":"premchand","nzame2":"aravindu"}
res24={j for i in u for j in u[i] if j in "aeiouAEIOU"}
print(res24)


u={"name1":"premchand","nzame2":"aravindu"}
res24={j for i in u for j in u[i] if j in "aeiouAEIOU"}
print(type(res24))



results=""
def vowel(leters):
    global results
    results+=leters
    return leters
v={"name1":"premchand","nzame2":"aravindu"}
res24={vowel(j) for i in v for j in u[i] if j in "aeiouAEIOU"}
print(res24)
    
