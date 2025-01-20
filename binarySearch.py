n=int(input("Enter the no of elements : "))
print("enter ",n,"numbers : ")
l=[]
for i in range (n):
    x=int(input())
    l.append(x)
tar=int(input("enter the target : "))
low=0
high=len(l)-1
f=0
while low<=high and f==0:
    mid=(low+high)//2
    if l[mid]==tar :
        print("element found at position : ",mid+1)
        f=1
    elif l[mid]>tar :
        high=mid-1
    else :
        low=mid+1
if f==0:
    print("element not found ")


