##Print an hourglass (sandglass) of stars.
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
    
    
##Outline version of sandglass.
# * * * * * 
#  *     * 
#   *   * 
#    * * 
#     * 
#    * * 
#   *   * 
#  *     * 
# * * * * * 

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
    
    
##Combine an upright and inverted right triangle.
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

n=4
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
    
##Print Pascal’s triangle for n = 5.
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   3   4   1

n=5
# p=1
for i in range(n):
    print(" "*(n-i),end="")
    p=1
    for j in range(i+1):
        print(p,end=" ")
        p=p*(i-j)//(j+1)
        
    print(" ")
    
    
    
    ##Print  triangle for n = 5.
#     1  
#   1 1  
#   1 2 1  
#  1 2 3 1  
# 1 2 3 4 1 

n=5
# p=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or j==i:
            print("1",end=" ")
        else:
            print(j,end=" ")
    print(" ")
    
    
    
##Floyd’s Triangle Print numbers continuously in triangle form.
# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15

n=5
p=1
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        print(p,end=" ")
        p+=1
    print(" ")
    
    
    
    
##Butterfly Pattern Symmetrical pattern using stars.
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


row=5
col=5
for i in range(1,row+1):
    for j in range(1,2*row+1):
        if j<=i or j>=(2*row-i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
for i in range(row-1,0,-1):
    for j in range(1,2*row+1):
        if j<=i or j>=(2*row-i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
##Butterfly Pattern Symmetrical pattern using stars.
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


n=5
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,2*n+1):
        if j<=i or j>=(2*n-i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    print(""*(n-i),end="")
    for j in range(1,2*n+1):
        if j<=i or j>=(2*n-i+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    
    
##Palindromic Number Pyramid Numbers increase and then decrease symmetrically.
#      1
#    1 2 1
#   1 2 3 2 1
#  1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
        
    print()
    
    
    
##Reverse Number Pyramid Centered numbers in descending triangle.
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
    
##Hollow Diamond Numbers Diamond with numbers at borders.
#     1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5
#  1     4
#   1   3
#    1 2
#     1


n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or j==1 or j==i or i==n:
            print(j,end=" ")
        else:
            print(" ",end=" ")
        
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        if i==1 or j==1 or j==i :
            print(j,end=" ")
        else:
            print(" ",end=" ")
        
    print()
    
    
    
    
    
##Pyramid with Continuous Numbers Numbers continue across all rows.
#       1
#      2 3
#     4 5 6
#   7 8 9 10
#  11 12 13 14 15

n=5
p=0
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        p+=1
        print(p,end=" ")
    print()