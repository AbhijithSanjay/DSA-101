'''
It's the end of the semester and you got your grades from three classes: Geometry, Algebra, and Physics.

Create a program that:

Reads the grades of these 3 classes (Grades range from 0 - 10)
Calculate the average of your grades

Example: Geometry = 6, Algebra = 7, Physics = 8
Output: average_score = 7
'''
geo=int(input("Enter the marks in Geometry : "))#accepting the marks of each subject
alg=int(input("Enter the marks in Algebra  : "))
phy=int(input("Enter the marks in Physics  : "))
print("average marks : ",(geo+alg+phy)/3) #printing the average marks