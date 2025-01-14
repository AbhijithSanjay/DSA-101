"""A cell phone company has the following billing policy

Fixed cost 25$
Call duration(in seconds)	Charge($/per second)
1-500	0,01
501-800	0,008
801+	0,005
Create a program that:

Reads how many seconds was the calls duration
Calculates the monthly bill for the subscriber
Prints the total amount
Output: total amount: 48$"""

call=int(input("Enter the call duration : "))
if call <= 500:
    print("total bill amount : ",call*0.01)
elif call<=800:
    print("total bill amount : ",(500*0.01)+((call-500)*0.008))
else:
    print("kljfs")
    print("total bill amount : ",(500*0.01)+(300*0.008)+((call-800)*0.005))