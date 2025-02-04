n=int(input("enter the no of rows"))
a=[]
for x in range(n):
    b = [None] * (x+1)
    b[0],b[x]=1,1
    for y in range(1,x):
        b[y]=a[x-1][y]+a[x-1][y-1]
    a.append(b)
for i in a:
    print(i)