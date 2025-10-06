##Print a 5×5 square using
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
    
    
    
##Print a rectangle of 3 rows and 6 columns.
# * * * * * *
# * * * * * *
# * * * * * *

row=3
col=6
for i in range(1,row+1):
    for j in range(1,col+1):
        print("*",end=" ")
    print()
    
    
    
##Print a right-angled triangle with stars.
# *
# * *
# * * *
# * * * *
# * * * * *

n=5
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
##Print a centred triangle with stars.
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *

n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
##Print right aligned  triangle with stars.
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
##Inverted Right-Angled Triangle
##Print the triangle upside down.
# * * * * *
# * * * *
# * * *
# * *
# *

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
##Inverted equal(centred)-Angled Triangle
##Print the triangle upside down.
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
##Inverted right aligned-Angled Triangle
##Print the triangle upside down.
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         *

n=5
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

    
##Right-Angled Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


##Right-Angled Number Triangle
#     1 
#   1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()


##Right-Angled Number Triangle
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5  
n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    
##Print rows where the same number repeats.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    
##Print rows where the same number repeats.
#     1 
#   2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 

n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


##Print rows where the same number repeats.
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5

n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


    
##Print continuous increasing numbers.
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n=4
p=0
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(p,end=" ")
    print()
    
    
    
    
##Print continuous increasing numbers.
#    1 
#   2 3 
#  4 5 6 
# 7 8 9 10 

n=4
p=0
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(p,end=" ")
    print()
    
    
    
##Print continuous increasing numbers.
#       1 
#     2 3 
#   4 5 6 
# 7 8 9 10 

n=4
p=0
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(p,end=" ")
    print()
    
    
    
##Print a 4×4 block of numbers.
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4


n=4
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,n+1):
        print(j,end=" ")
    print()
    
    
    
    
    
##Print alphabets in a triangle shape.
# A
# A B
# A B C
# A B C D
# A B C D E

n=5

for i in range(1,n+1):
    print(""*(n-i),end="")
    p=64
    for j in range(1,i+1):
        print(chr(p+j),end=" ")
    
    print()
    
    
    
##Print alphabets in a triangle shape.
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 

n=5

for i in range(1,n+1):
    print(" "*(n-i),end="")
    p=64
    for j in range(1,i+1):
        print(chr(p+j),end=" ")
    
    print()




##Print alphabets in a triangle shape.
#         A 
#       A B 
#     A B C 
#   A B C D 
# A B C D E  

n=5

for i in range(1,n+1):
    print("  "*(n-i),end="")
    p=64
    for j in range(1,i+1):
        print(chr(p+j),end=" ")
    
    print()
    
    
    
##Print alphabets in a triangle shape.
#     A 
#    A A 
#   A A A 
#  A A A A 
# A A A A A  

n=5

for i in range(1,n+1):
    print(" "*(n-i),end="")
    p=64
    p+=1
    for j in range(1,i+1):
        print(chr(p),end=" ")
    
    print()
    
    
##Print alphabets in a triangle shape.
# A 
# B B 
# C C C 
# D D D D 
# E E E E E  

n=5
p=64
for i in range(1,n+1):
    print(""*(n-i),end="")
    p+=1
    for j in range(1,i+1):
        print(chr(p),end=" ")
    
    print()
    
    
    
##Print alphabets in a triangle shape.
#     A 
#   B B 
#   C C C 
#  D D D D 
# E E E E E  

n=5
p=64
for i in range(1,n+1):
    print(" "*(n-i),end="")
    p+=1
    for j in range(1,i+1):
        print(chr(p),end=" ")
    
    print()
    
    
    
##Print alphabets in a triangle shape.
#         A 
#       B B 
#     C C C 
#   D D D D 
# E E E E E  

n=5
p=64
for i in range(1,n+1):
    print("  "*(n-i),end="")
    p+=1
    for j in range(1,i+1):
        print(chr(p),end=" ")
    
    print()
    
    
    
    
##Print alphabets in a triangle shape.
# A 
# B C 
# D E F 
# G H I J 
# K L M N O  

n=5
p=64
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()
    
    
    
##Print alphabets in a triangle shape.
#     A 
#    B C 
#   D E F 
#  G H I J 
# K L M N O   

n=5
p=64
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()   
    
    
    
    
##Print alphabets in a triangle shape.
#         A 
#       B C 
#     D E F 
#   G H I J 
# K L M N O   

n=5
p=64
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()
    
    
    
    
    
    
##Inverted Alphabet Triangle
# A B C D E 
# A B C D 
# A B C 
# A B 
# A   

n=5
# p=64
for i in range(n,0,-1):
    print(""*(n-i),end="")
    p=64
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()




##Inverted Alphabet Triangle
# A B C D E 
#  A B C D 
#   A B C 
#   A B 
#     A   

n=5
# p=64
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    p=64
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()
    
    
    
    
    
##Inverted Alphabet Triangle
# A B C D E 
#   A B C D 
#     A B C 
#       A B 
#         A   

n=5
# p=64
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    p=64
    for j in range(1,i+1):
        p+=1
        print(chr(p),end=" ")
    
    print()