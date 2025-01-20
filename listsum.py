n=int(input("Enter the no of elements : "))
print("enter ",n,"numbers : ")
l=[]
for i in range (n):
    x=int(input())
    l.append(x)
print(l)
sum=int(input("enter the sum to search : "))
f=0
for i in range(0,n):
    for j in range(i+1,n):
        x=l[i]+l[j]
        if sum == x :
            print("sum found between ",l[i],"and",l[j])
            f=1
if f==0:
    print("sum not found in list")

        
    