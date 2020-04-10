'''
Write a number prettifier:

Write tested code that accepts a numeric type and returns a truncated, "prettified" string version.
The prettified version should include one number after the decimal when the truncated number is not an integer.
It should prettify numbers greater than 6 digits and support millions, billions and trillions.

Examples:
   input: 1000000
   output: 1M

   input: 2500000.34
   output: 2.5M

   input: 532
   output: 532

   input: 1123456789
   output: 1.1B

   input: 9487634567534
   output: 9.5T
'''


def get_input():
    """ Get a numerical value from the user.

            Params: None.

            Return:
                user_input_num (float): The raw number that a user entered.
    """
    # This ensures that only numerical values are allowed.
    try:
        user_input_num = float(
            input("Enter a number without any punctuation. Can handle large numbers up to and including trillions: "))

        return user_input_num
    except ValueError:
        print("Please enter a numerical value.")


def pretty_format(num):
    """ Convert numbers to a human readable, "pretty" format.
        It will prettify numbers greater than 3 digits and supports thousands, millions, billions and trillions.

            Params:
                num (float): the raw number to be converted
            Return:
                pretty_string (string): prettified string, e.g. "1M" or "1.3B"
    """

    # Round to 1 digit after the decimal point
    round_to = 1

    # {0} tells format to print the first argument in this case "num" and .3 sets the precision to 3
    num = float('{:.3g}'.format(num))

    suffix = ['', 'K', 'M', 'B', 'T']

    magnitude = 0
    while abs(num) >= 1000:
        # Count the order of magnitude to determine which suffix to use
        magnitude += 1

        # Use `round` for rounding (beyond the decimal point if necessary)
        num = round(num / 1000.0, round_to)

        pretty_string = '{}{}'.format('{:.1f}'.format(num).rstrip('0').rstrip('.'), suffix[magnitude])

        # Cap the number. Can't exceed the positive or negative trillions.
        len_string = len(pretty_string)
        if (len_string > 13 and num > 0) or (num < 0 and len_string > 14):
            raise IndexError('Number cannot exceed the trillions. Enter a smaller value.')

    return '{}{}'.format('{:.1f}'.format(num).rstrip('0').rstrip('.'), suffix[magnitude])


user_input = get_input()
pretty_number = pretty_format(user_input)
print('input: ', user_input, '\n' 'output: ', pretty_number)