"""The exercise is almost identical to a previous exercise with a minor change.
In a company the monthly salary of an employee is calculated by minimum wage 400$ per month, 
plus 20$ multiply by the employment years, plus 30$ for each employee kid, plus 100$ if the employee
didn't miss 1 day of work.

Create a program that:

Reads the employment years
Reads the number of each employee kids
Prints the total amount the employee must take
Output: "The total amount is 660$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids 
+ 100$ for not missing a day at work"""

exp=int(input("enter the employment year : "))
kid=int(input("enter the no of kids : "))
x=int(input("did you miss any day (0 for no/1 for yes) :"))
if bool(x):
    print("salary : ",(exp*20)+400+(kid*30))
else:
    print("salary : ",(exp*20)+400+(kid*30)+100)
