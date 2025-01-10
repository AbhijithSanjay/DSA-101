"""The exercise is almost identical to a previous exercise with a minor change. It's the end of 
the semester and you got your marks from, Geometry, Algebra, Physics classes. If the average score 
is 7 and above print "Good job!", if the average score is between 6 and 4 print "You need to work 
harder!", if the average score is below 4 print "Failed, you really need to work harder!".

Create a program that:

Reads the values of these 3 lessons
Calculate the average of your grades
Example: Geometry = 6, Algebra = 7, Physics = 8
Output: Your average score is 7, Good job!"
Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.
"""
print("entered marks should be between 0 and 10")
geo=int(input("Enter the marks in Geometry : "))#accepting the marks of each subject
alg=int(input("Enter the marks in Algebra  : "))
phy=int(input("Enter the marks in Physics  : "))
avg=(geo+alg+phy)/3 #calculating average
print("average marks : ",avg)
if avg>=7 and avg<=10:#printing evaluation based on average marks
    print("Good job!")
elif avg<7 and avg>=4:
    print("You need to work harder!")
elif avg<4:
    print("Failed, You really need to work harder!!")
else:
    print("You entered your marks incorrectly")