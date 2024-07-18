print("Welcime to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = total_bill + (total_bill * (tip / 100))
per_person_bill = "{:.2f}".format(bill_with_tip / no_of_people)

print(f"Each person should pay: ${per_person_bill}")
