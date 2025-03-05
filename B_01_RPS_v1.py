def string_checker(question, valid_ans=("yes", "no")):
    """A simple string checker that defaults to 'yes' and 'no'."""

    error = f"\nThis is not a valid input, please enter a valid answer from the list: {valid_ans}\n"

    while True:

        user_response = input(question).lower()

        for i in valid_ans:
            # check if the users response is in the word list
            if i == user_response:
                return i

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == i[0]:
                return i

        print(error)


def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


def int_check(question, low):
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

            if answer < low:
                print(error)

            else:
                return answer

        # if an integer was not inputted it will print the error
        except ValueError:

            print(error)


def instructions():
    """Asks and displays instructions"""

    # Asks if the user wants instructions
    want_instructions = string_checker("Do you want instructions? ")

    # Prints instructions if they say yes
    if want_instructions == "yes":

        statement_generator("*", 3, "Instructions")
        print(''' First choose a number of rounds to play or press <enter> for infinite mode

Then select 'rock', 'paper', or 'scissors'.

-    'rock' beats 'scissors'
-    'scissors' beats 'paper'
-    'paper' beats 'rock'

Enter "xxx" to exit.
        ''')


# Main routine goes here

# Heading
print("\n🪨/📄/✂️ Rock, Paper, Scissors 🪨/📄/✂️\n")

# Ask if the user wants instructions and if they do display them

instructions()

# Initialise yes no list
rps_list = ["rock", "paper", "scissors", "xxx"]

# Asks how many game rounds
game_rounds = int_check("How many rounds do you want to play (press <enter> for infinite)? ", 1)

# If infinite mode is selected loops until "xxx" is entered if the game mode is set to infinite
if game_rounds == "":

    rounds_played = 0

    while True:

        # Round counter
        rounds_played += 1

        # Nice heading
        statement_generator("🔃", 3, f"Infinite Mode (Round: {rounds_played})")

        # Gets choices
        choice = string_checker("Choice: ", rps_list)

        # Exit code to break
        if choice == "xxx":
            break


else:

    # Heading
    statement_generator("🔃", 3, f"{game_rounds} Rounds")

    # loops the desired amount of times
    for item in range(0, game_rounds):

        # Sets the round number
        round_number = item + 1

        # Prints round number
        statement_generator("🔃", 3, f"Round: {round_number}")

        # Asks for their choice
        choice = string_checker("Choice: ", rps_list)

        # Exit code to break
        if choice == "xxx":
            break

