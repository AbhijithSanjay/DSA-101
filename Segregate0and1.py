a=[1,0,1,1,0,1,0,0,0,1]
b=a[:]
i=0
j=len(a)-1
for x in a:
    if x==0:
        b[i]=x
        i+=1
    else:
        b[j]=x
        j-=1
print(b)
