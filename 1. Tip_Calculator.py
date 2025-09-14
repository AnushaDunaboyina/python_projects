print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
each_person_bill = (bill + ((bill * tip)/100)) / people
print("Each person should pay : $" , round(each_person_bill,2))


# using f-string
# print(f"Each person should pay : ${round(each_person_bill,2)}")