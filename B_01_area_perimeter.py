# Ask user fpr width and loop until they
#enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more thaan zero\n"
    while True:

        try:
            #ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)


        except ValueError:
         print(error)


# Main Routine starts hre...

keep_going = ""
while keep_going == "":

    #Get width and height
    width = num_check("width: ")
    height = num_check("height: ")

    #Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    #Output the area and perimeter
    print()
    print(f"Perimeter {perimeter} units")
    print(f"Area: {area} square units")

    #Ask user if they want to keep going

    keep_going = input("Press enter to keep going or ant key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")