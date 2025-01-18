
n=int(input("no of elements in fibonacci series to be printed : "))
x=0
y=1
next=1
print(x)
print(y)
while n-2 !=0:
    print(next)
    x,y=y,next
    next=x+y
    n-=1

