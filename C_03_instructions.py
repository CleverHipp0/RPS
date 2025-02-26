def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


def yes_no(question):
    """Input question, out put whether they said yes or no"""
    while True:

        # Asks a yes or no question
        yes_no_raw = input(question).lower()

        # acceptable answers in lists
        yes_acceptable = ("yes", "y")
        no_acceptable = ("no", "n")

        # Checks the list to see if it's an acceptable answer and returns it
        if yes_no_raw in yes_acceptable:
            return yes_acceptable[0]

        elif yes_no_raw in no_acceptable:
            return no_acceptable[0]

        else:
            print("That is not an acceptable answer. Please answer with <yes> or <no>.")\



def instructions():
    """Asks and displays instructions"""

    # Asks if the user wants instructions
    want_instructions = yes_no("Do you want instructions? ")

    # Prints instructions if they say yes
    if want_instructions == "yes":

        statement_generator("*", 3, "Instructions")
        print('''- 1
- 2
- 3
        ''')


# Main routine goes here

instructions()

