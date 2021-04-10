# find sum of numbers located on diagonals
def spiralize(number):
    # finding diagonals
    x = (number - 1) / 2
    # formula for sum of diagonals
    y = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3

    return_value = y
    return return_value
