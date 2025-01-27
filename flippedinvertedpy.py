n=int(input("Enter the no of rows : "))
for i in range(n,0,-1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for x in range(0,i):
        print("*",end=" ")
    print()