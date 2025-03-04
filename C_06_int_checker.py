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


rounds = int_check("Number of rounds: ", 1)
if rounds == "":
    print("infinite")

else:
    print(rounds)
