"""You've bought a Bitcoin and now it's on the rise!!!

Create a program that:

Reads the value of the bitcoin at the time of purchase
Reads the percentage of increase (or decrease)
Prints the total value of your bitcoin
Prints the increase or decrease value
Example: bitcoin_value = 10000, bitcoin_increase = 10
Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000"""

iniVal=int(input("Enter the initial value of the Bitcoin       : "))#accepting input values
per=int(input("Enter the percentage of increase or decrease :"))
CurVal=iniVal*(1+(per/100))#calculation of current value of Bitcoin
print("Current value of Bitcoin : ",CurVal)
print("Bitcoin Value changed by : ",CurVal-iniVal)#calculating and printing the amount by which the value of bitcoin changed