#ask the user fpt their name
username = input("What is your name? ")

#ask the user for their favorite number (interger)
fav_num = int(input("What is your favorite number? "))

#Double,  halve and square the user's favorite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num
# Greet the user
print(f"HI {username}, your favorite number is {fav_num}")

#Output the reasults of doubling, halving and squaring their favorite integer

print(f"Double {fav_num} is {double}")
print(f"Half {fav_num} is {halve}")
print(f"{fav_num} squared is {square} ")
print()
print("Have a nice day.")