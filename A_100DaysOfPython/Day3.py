#Copy paste area
#-- 
print("\n-----------------------------------------")
#Copy paste area


#Day 3 of learning


#if/else statements 
#-- print("Welcome to the rollercoaster!")
#-- height = input("What is your height in cm? ")

#-- if int(height) >= 120:
#--     print("You can ride the rollercoaster!")
#-- else:
#--     print("You cannot ride the rollercoaster because you are SHOOORT!")

print("\n-----------------------------------------")

#Exercise - Odd or Even 
#Don't change the code below
#-- number = int(input("Which number should we check: "))
#Don't change the code below

#This is my Solution
#-- if number % 2 == 0:
#--     print ("This is an even number.")
#-- else:
#--     print ("This is an odd number.")

print("\n-----------------------------------------")

#Nested if/else , elif
#-- height = int(input("What is your height in cm?: "))
#-- age = int(input("What is you age?: "))

#-- if height >= 120:
#--     print("You can ride the rollercoaster!")
#--     if age < 12:
#--         print ("Please pay $5.")
#--     elif age <= 18:
#--         print("Please pay $7")
#--     else:
#--         print("Please pay $12.")
#-- else:
#--     print("You cannot ride the rollercoaster because you are SHOOORT!")

#Exercise - BMI 2.0 
#Don't change the code below
#-- height = input ("enter your height in m: ")
#-- weight = input ("enter your weight in kg: ")
#Don't change the code above

#My solution code below 
#-- bmi =  float(weight) / float(height) ** 2
#-- result = round(bmi , 2)

#-- if result < 18.5:
#--     print(f"Your BMI is {result}, You are underweight")
#-- elif result > 18.5 and result < 25:
#--     print(f"Your BMI is {result}, You have normal weight")
#-- elif result > 25 and result < 30:
#--     print(f"Your BMI is {result}, You are overweight")
#-- elif result > 30 and result < 35:
#--     print(f"Your BMI is {result}, You are obese")
#-- else:
#--     print(f"Your BMI is {result}, You are clinically obese")

print("\n-----------------------------------------")

#Don't change the code below
#-- year = int(input("Which year do you want to check?: "))
#Don't change the code above

#My solution code below 

#-- if year % 4 == 0:
#--     if year % 100 == 0:
#--         if year % 400 == 0:
#--             print("Leap because divisible by 400")
#--         else:
#--             print("Not leap because divisible by 100 but not 400")
#--     else:
#--         print ("Leap because divisible by 4 but not 100")
#-- else:
#--     print("Not leap because not divisible by 4 at all")


print("\n-----------------------------------------")

#Exercise - Pizza Order 
#Don't change the code below
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# #Don't change the code above

# #My solution code
# bill = 0
# add_bill = 0

# if size == 's' or size == 'S':
#     bill += 15

# elif size == 'm' or size == 'M':
#     bill += 20

# elif size == 'l' or size == 'L':
#     bill += 25 

# if add_pepperoni == 'y' or add_pepperoni =='Y':
#     add_bill += 2

# if extra_cheese == 'y' or extra_cheese == 'Y':
#     add_bill += 3

# print(f"Your total bill is: {bill + add_bill}")

print("\n-----------------------------------------")

#Exercise - Love Calculator
#Don't change the code below
# score = 0
# print("Welcome to the Love Calculator!")
# name1 = input("What is your first name?: ")
# name2 = input("What is their first name?: ")
# #Don't change the code above

# #My solution code 
# combine = name1.lower() + name2.lower()

# t = combine.count('t')
# r = combine.count('r')
# u = combine.count('u')
# e = combine.count('e')
# l = combine.count('l')
# o = combine.count('o')
# v = combine.count('v')
# e = combine.count('e')

# true_total = t + r + u + e
# love_total = l + o + v + e

# score = int(str(true_total) + str(love_total))

# if score < 10 or score > 90:
#     print(f"Your love score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
