n=int(input("Enter the no of lines : "))
for x in range (n,0,-1):
    for i in range(n-x,0,-1):
        print(" ",end=" ")
    for j in range(0,(2*x-1)):
        print("*",end=" ")
    print("\n")