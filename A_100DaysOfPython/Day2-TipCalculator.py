#TIP CALCULATOR

# Day 2 Project

print("Welcome to the tip calculator.\n")
bill = input("What was the total bill? $:")
tip = input("What percentage tip would you like to give?\n10, 12, or 15?:")
split = input("How many people to split the bill?: ")


tip_amount = (float(tip) / 100) * float(bill) 
add_tip = tip_amount + float(bill)
total = add_tip / int(split)


print(f"each person should pay:${total:.2f}")
