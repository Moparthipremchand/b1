##Pyramid (Centered Stars)
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
    
    
    
##Inverted Pyramid
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
    
    
    
    
    
    
##Hollow Square Only the border should show stars.
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
##Hollow Right-Angled Triangle
# *
# * *
# *   *
# *     *
# * * * * *


n=5
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
##Hollowcentred Triangle
#     * 
#    * * 
#   *   * 
#  *     * 
# * * * * * 


n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    

##Hollow Right-Angled Triangle
#         * 
#       * * 
#     *   * 
#   *     * 
# * * * * *  


n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
##Hollow Inverted Triangle
# * * * * * 
# *     * 
# *   * 
# * * 
# *  


n=5
for i in range(n,0,-1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
##Hollow Inverted centred Triangle
# * * * * * 
#  *     * 
#   *   * 
#    * * 
#     * 



n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
##Hollow Inverted Triangle
# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 



n=5
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
##Print a centered number pyramid.
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5




n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    
    
##Print continuous numbers in a pyramid form.
#     1
#    2 3
#   4 5 6
#  7 8 9 10


n=4
p=0
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(p,end=" ")
    print()
    
    
    
    
##Pyramid using alphabets.
#     A
#    A B
#   A B C
#  A B C D
# A B C D E



n=5
p=64
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        # p+=1
        print(chr(p+j),end=" ")
    print()
    
    
    
##Pyramid using alphabets.
#     A 
#    B B 
#   C C C 
#  D D D D 
# E E E E E 



n=5
p=64
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        # p+=1
        print(chr(p+i),end=" ")
    print()
    
    
    
    
##Pyramid using alphabets.
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
    
    
    
##Diamond Shape (Stars)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *




n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
    
    
##Diamond outline only.
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or  j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()