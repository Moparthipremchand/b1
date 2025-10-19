## Diamond Number-Star Mix: Numbers increase and decrease symmetrically with stars filling the rest.
#     1
#    2*2
#   3***3
#  4*****4
# 5*******5
#  4*****4
#   3***3
#    2*2
#     1

n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if i==1 or j==1 or j==2*i-1:
            print(i,end="")
        else:
            print("*",end="")
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(1,2*i):
        if i==1 or j==1 or j==2*i-1:
            print(i,end="")
        else:
            print("*",end="")
    print()
    
    
    
    
    
## Double-Sided Number Pyramid: Numbers mirror on both sides with spaces between.
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n=5
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print(" " * (2 * (n - i)), end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
    
    
## Hourglass Numbers: Numbers form a descending and ascending hourglass.
# 12345
#  1234
#   123
#    12
#     1
#    12
#   123
#  1234
# 12345


n=5
for i in range(n,1,-1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
    
    
# Alphabet version of butterfly pattern.
# A        A
# A B      B A
# A B C    C B A
# A B C D  D C B A
# A B C D E C D B A
# A B C D  D C B A
# A B C    C B A
# A B      B A
# A        A
n=5
for i in range(1,n+1):
    # print(""*(n-i),end="")
    
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print("  " * (n - i), end=" ")
     
    for j in range(i,0,-1):
        print(chr(64+j),end=" ")
        
    print()
for i in range(n-1,0,-1):
    # print(""*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print("  " * (n - i), end=" ")
     
    for j in range(i,0,-1):
        print(chr(64+j),end=" ")
        
    print()
    
    
    
# Pyramid with borders as numbers only.
#         1
#       1   2
#     1       3
#   1           4
# 1 2 3 4 5 4 3 2 1
n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==1 or i==n :
            print(j, end=" ")
        else:
            print(" ", end=" ")
        # print("  " * (n - i), end=" ")
    for j in range(i - 1, 0, -1):
        if  j == 1 or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
    
    

    # Concentric Number Square
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4
n=7
for i in range(1,n+1):
    print(""*(n-i),end="")
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("4",end=" ")
        elif i==2 or i==6 or j==2 or j==6:
            print("3",end=" ")
        elif i==3 or i==5 or j==3 or j==5:
            print("2",end=" ")
        else:
            print("1",end=" ")
    print()
    
    

