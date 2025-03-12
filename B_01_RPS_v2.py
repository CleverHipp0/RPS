import random


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


def rps_compare(user_input, comp_input):
    """Compares two inputs to a list"""

    if user_input == comp_input:
        return "tie"

    elif user_input == "paper" and comp_input == "rock":
        return "win"

    elif user_input == "scissors" and comp_input == "paper":
        return "win"

    elif user_input == "rock" and comp_input == "scissors":
        return "win"

    else:
        return "lose"


def game_to_loop():
    """Asks for the two choices and compares them. If the exit code is entered it will return it"""

    # Asks for their choice
    user_choice = string_checker("Choice: ", rps_list)
    print()
    # Exit code to break
    if user_choice == "xxx":
        return "exit"

    else:
        # Random choice for the computer from the rps list (excluding exit codes)
        comp_choice = random.choice(rps_list[:-1])
        results = rps_compare(user_choice, comp_choice)
        statement_generator("🎖️", 3, "Results")
        print(f"User: {user_choice} | Comp: {comp_choice} | You {results}\n")
        return results, comp_choice, user_choice


# Main routine goes here

# Heading
print("\n🪨/📄/✂️ Rock, Paper, Scissors 🪨/📄/✂️\n")

# Ask if the user wants instructions and if they do display them

instructions()

# Initialise yes no list
rps_list = ["rock", "paper", "scissors", "xxx"]
mode = "regular"

rounds_played = 0
won = 0
lost = 0
tied = 0

comp_history = []
history = []

# Asks how many game rounds
game_rounds = int_check("How many rounds do you want to play (press <enter> for infinite)? ", 1)

# If infinite mode is selected loops until "xxx" is entered if the game mode is set to infinite
if game_rounds == "":
    mode = "infinite"
    game_rounds = 5
    heading = "Infinite Mode"

else:
    heading = f"{game_rounds} Rounds"

statement_generator("🔃", 3, heading)

while True:

    # Round counter
    rounds_played += 1

    # Nice heading
    statement_generator("🔃", 3, f"Round: {rounds_played}")

    # Runs the game until the exit code is entered
    returned_results = game_to_loop()
    if returned_results == "exit":
        break

    elif returned_results[0] == "win":
        won += 1

    elif returned_results[0] == "tie":
        tied += 1

    else:
        lost += 1

    history.append(returned_results)

    if mode != "infinite" and rounds_played == game_rounds:
        break


statement_generator("📈", 3, "Stats")


percent_won = (won / rounds_played) * 100
percent_lost = (lost / rounds_played) * 100
percent_tied = (tied / rounds_played) * 100

print(f"Percent won: {percent_won:.2f} | Percent lost: {percent_lost:.2f} | Percent tied: {percent_tied:.2f}")


history_show = string_checker("Do you want to see the game history? ")
print()

if history_show == "yes":

    count = 0
    statement_generator("🛞", 3, "History")

    for item in history:

        print(f"\nRound: {count + 1}")
        print(f"User choice: {item[1]} | Comp choice: {item[2]} | You: {item[0]}")
        count += 1





