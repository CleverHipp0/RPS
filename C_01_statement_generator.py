def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}\n")


# --- Hello world ---
# -
# Hello world
# 3

statement_generator("-", 3, "Hello world")



