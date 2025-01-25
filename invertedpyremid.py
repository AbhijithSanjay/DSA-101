n=int(input("enter the size: "))
for x in range(0,n):
    for y in range(0,n-x):
        print("*",end=" ")
    print()
