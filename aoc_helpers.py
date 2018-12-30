def get_input(day):
    """Takes in the day, returns the corresponding input as a string"""

    filename = "inputs/day-%s" % day
    with open(filename) as input_file:
        return input_file.readlines()
