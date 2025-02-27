def int_check(question):
    """Checks for a number more than 0, accepts <enter> for infinite"""

    # Sets up an error message
    error = "Please enter an whole number or <enter>."

    while True:

        # Asks the question
        answer = input(question)

        # Returns if they input <enter>
        if answer == "":
            return answer

        # Checks to see if they entered an integer
        try:
            answer = int(answer)
            return answer

        # if an integer was not inputted it will print the error
        except ValueError:

            print(error)


# Main routine goes here

# Asks how many game rounds
game_rounds = int_check("How many rounds do you want to play (press <enter> for infinite)? ")

# loops until "xxx" is entered if the game mode is set to infinite
if game_rounds == "":

    while True:
        choice = input("Choice: ")

        if choice == "xxx":
            break

# loops the desired amount of times
else:

    for item in range(0, game_rounds):
        choice = input("Choice: ")



