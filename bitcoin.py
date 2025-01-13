"""You are interested in buying crypto-currencies. You want to check the current amount of money 
you have and see how many coins you can buy in Bitcoin, Ethereum, and Litecoin.

Create a program that:

Reads the total amount of money you have
Reads the price of Bitcoin, Ethereum, and Litecoin
Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy
Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"""

tot=int(input("enter the total money with you :"))
bit=int(input("enter the value of bitcoin   : "))
eth=int(input("enter the value of ethereum  : "))
lit=int(input("enter the value of lite coin : "))
print("with ",tot," you can buy : ",tot//bit," Bitcoin , ",tot//eth," ethereum, and ",tot//lit," Lite coins")
