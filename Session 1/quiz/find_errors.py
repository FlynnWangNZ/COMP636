print("Please input two positive numbers and I'll add them up for you!\n")
first_number = float(input("Please enter your first number: "))
second_number = float(input("Please enter your second number: "))
        
if (first_number >= 0 and second_number >= 0):
    print("The result of adding your numbers together is: " + str(first_number + second_number))
else:
    print("At least one of those numbers was not positive, please try again. Goodbye!")
