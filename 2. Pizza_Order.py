print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L: ").lower()

small = 10
middle = 12
large = 15
pepperoni1 = int(3)
extra_cheese = int(2)

bill = 0

if size == "s":
    bill += small
elif size == "m":
    bill += middle
else:
    bill += large

print ("$",bill)

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == "y":
    bill += pepperoni1
else:
    bill += 0

print("$",bill)

cheese = input("Do you want extra cheese? Y or N: ").lower()
if cheese == "y":
    bill += extra_cheese
else:
    bill += 0

print("Total bill : $",bill)
