# Shipping-Charges
 Calculates shipping charges based on a package's weight.

## Scope
The Fast Freight Shipping Company charges the following flat rates to ship a package:

    |============================================================|
    |Weight of Package                       | Flat Rate Price   |
    |----------------------------------------|-------------------|
    |Less than 2 pounds                      |       $5.50       |
    |----------------------------------------|-------------------|
    |2 pounds and over, but under 6 pounds   |       $7.00       |
    |----------------------------------------|-------------------|
    |6 pounds and over, but under 10 pounds  |       $9.75       |
    |----------------------------------------|-------------------|
    |10 pounds and over                      |      $15.50       |
    |============================================================|

Write a program that asks the user to enter the weight of a package, then have the program display the flat rate shipping charge for the package.

Your program must contain an if statement.

## Sample Run
    This program calculates the flat shipping rate of a package.
    Enter the weight of the package in pounds: 6.8

    The shipping charge for this package is: $9.75

## Pseudocode
### Main program logic
    START
      INPUT Weight of a package in lbs.
      CALL shipping_price function
      PRINT shipping charge
    END

### shipping_price function
    START
      PASS IN: package weight
      IF package weight is less than 2 lbs
        price = $5.50
      ELSE
        IF package weight is greater or equal to 2 but less than 6
          price = $7.00
      ELSE
        IF package weight is greater or equal to 6 but less than 10
          price = $9.75
      ELSE
        price = $15.50
      ENDIF
      RETURN price
    END
