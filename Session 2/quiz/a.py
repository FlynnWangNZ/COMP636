character_name = "SpiderMan"
len_name = len(character_name)
print("Welcome to the fictional character guessing game.\n")
print("I'm thinking of a super hero from a film, have a guess who I am thinking of.")

guessed = False;
hint_counter = 0;
while not guessed:
    name_guessed = input("Enter your guess or hint if you need some help: ")
    if (name_guessed.lower().strip() == 'hint'):
        hint_counter +=1
        if hint_counter == 1:
            print("Marvel Cinematic Universe\n")
        elif hint_counter==2:
            print("Male\n")
        elif hint_counter==3:   
            print("Student\n")
        elif hint_counter ==4:
            print("Silk\n")
        else:
            print("Sorry that is all my hints!")
    else:
        if len(name_guessed) < len_name:
            print("I'm thinking of a longer name\n")
        elif len(name_guessed)> len_name:
            print("That name is too long\n")
        else:
            if name_guessed.lower().strip()==character_name.lower():
                guessed = True
                print("Well Done, you guessed what I was thinking of, just right!")
            else:
                print("That name is the right length, but isn't the one I'm thinking of")
