# Shipping Charges
# Shaun Hayworth
# CIS 2
# 12-02-2019
# Source code and revision history are available at
# https://github.com/SCHayworth/Shipping-Charges

# This program calculates shipping costs based on the weight in pounds of a
# package.


# Define the main function
def main():
    '''This is the mainline program logic.
    '''
    # Display descriptive message.
    print('This program calculates the flat shipping rate of a package.')

    # Prompt user for the weight of a package in lbs.
    package_weight = float(input('Enter the weight of a package in pounds: '))

    # Call the shipping_price function and pass the weight to it, then print
    # the result to the screen.
    shipping_rate = shipping_price(package_weight)
    print(f'The shipping charge for this package is: ${shipping_rate:.2f}')


# Define the shipping_price function.
def shipping_price(weight):
    '''Calculates the shipping rate given the weight of a package.
    '''
    # Determine the shipping rate and return the value.
    if weight < 2:
        price = 5.5
    elif weight >= 2 and weight < 6:
        price = 7
    elif weight >=6 and weight < 10:
        price = 9.75
    else:
        price = 15.5
    return price

# Call the main() function to execute the program.
main()
