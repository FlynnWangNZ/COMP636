username = input("Please enter your name: ")
print("hello, " + username)

favnumber = input("Please enter your favourite number: ")
print("Your number is: " + str(favnumber))

print("My lucky number is 11. Let's add them together.")

result = int(favnumber) + 11
print("Finally we get the result of " + str(result))


if result == 18:
    print("they are perfect combinations")
else:
    print("I have got better combinations")
