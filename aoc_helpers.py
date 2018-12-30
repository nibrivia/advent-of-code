def get_input(day):
    """Takes in the day, returns the corresponding input as a string"""

    filename = "inputs/day-%s" % day
    with open(filename) as input_file:
        return input_file.readlines()


def dict_key(entry):
    """Allows to returns a sorted dictionnary"""
    key, value = entry
    return value

def sort_dict(d):
    """Returns a list of (key, elemen"""
    return sorted(d.items(), key = dict_key)
