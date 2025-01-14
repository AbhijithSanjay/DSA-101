"""You want to buy something from Amazon. The seller charges different prices for shipping cost 
based on location. For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$

Create a program that:

Reads the cost of the product
Reads your location
Print the amount of money you have to pay
Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost"""

cost=int(input("enter the cost of product : "))
location=input("Enter the location : ")
match location:
    case "us":
        print("you have to pay ",cost+5,"$")
    case "europe":
        print("you have to pay ",cost+7,"$")
    case "canada":
        print("you have to pay ",cost+3,"$")
    case default :
        print("you have to pay ",cost+9,"$")