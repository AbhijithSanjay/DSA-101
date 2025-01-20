n=int(input("Enter the no of elements : "))
print("enter ",n,"numbers : ")
l=[]
for i in range (n):
    x=int(input())
    l.append(x)
target=int(input("enter the target : "))
for x in range(n):
    if l[x]==target:
        print("target found at the position : ",x+1)