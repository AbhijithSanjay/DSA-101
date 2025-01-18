n=int(input("enter a number : "))
rev=0
m=n
while n!=0:
    rev=(rev*10)+(n%10)
    n=n//10
if m==rev:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
