import os
import math

os.system('cls')

def calculateMonthsUntilPaidOff(bal,apr,monthlyPayment):
	balance = bal
	daily_rate = apr / 100 / 365
	monnthly_payment = monthlyPayment
	
	num_of_months = (-1/30) * (math.log(1 + ((balance/monnthly_payment)) * (1 - ((1 + daily_rate)**30)))
            /math.log(1 + daily_rate))

	return num_of_months

balance = int(input("What is your balance? "))
apr = int(input("What is the APR on the card (as a percent)? "))
monnthly_payment = int(input("What is the monthly payment you can make? "))

months_to_pay_off = math.ceil(calculateMonthsUntilPaidOff(balance,apr,monnthly_payment))

print(f"It will take you {months_to_pay_off} monhts to pay off this card.")



