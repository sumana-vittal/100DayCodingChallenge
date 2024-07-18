age = input()

# Write your code below this line 👇
total_weeks = 90 * 52
your_weeks_passed = int(age) * 52
weeks_left = total_weeks - your_weeks_passed
print(f"You have {weeks_left} weeks left.")
