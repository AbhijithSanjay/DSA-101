n=int(input("Enter the no of lines : "))
for x in range (1,n+1):
    for i in range(0,n-x):
        print(" ",end=" ")
    for j in range(0,(2*x-1)):
        print("*",end=" ")
    print("\n")