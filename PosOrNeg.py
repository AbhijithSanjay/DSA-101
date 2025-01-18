num=[]
out=[]
print("enter 5 numbers :")
for i in range(5):
    n=int(input())
    num.append(n)
print(num)
for x in range(5):
    if num[x]>0:
        out.append("positive")
    elif num[x]<0:
        out.append("negative")
    else:
        out.append("zero")
print(out)
