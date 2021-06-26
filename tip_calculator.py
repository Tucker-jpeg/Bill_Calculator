#!/usr/bin/env python3.7.6
# Python implementation here

print("Welcome To The Bill Split Calculator")

#Prompt the user to enter the amount on the bill
total_bill = float(input("What is the total bill?: "))

#Prompt the user for the % tip they'd like to leave
percentage_tip = int(input("What % tip would you like to give?: "))

#Prompt the user for the # of people splitting the bill
number_of_people = int(input("How many people are splitting the bill?: "))
print("\n")
#Calculate the value each person owes based on the bill and tips the user entered
payment_per_person = ("%.2f" % round(float(((percentage_tip / 100 +1) * total_bill) / number_of_people), 2))

#Print the $ amount of the tip
tip_amount = "%.2f" % float(percentage_tip / 100 * total_bill)
print(f"Tip amount: ${tip_amount}")

#convert total bill and tip amount to floats so they can be added
total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: ${tip_and_total}")

print(f"Each person owes: ${payment_per_person}")
