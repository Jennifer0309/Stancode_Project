"""
File: quadratic_solver.py
Name:jennifer Li
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equatthe ion:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
    """
    This program takes the coefficients a, b and c from the user,
    calculates the discriminant, and then determines the roots based on the value of the discriminant:
    If the discriminant is greater than zero, it calculates and displays two real roots.
    If the discriminant is equal to zero, it calculates and displays one real root.
    If the discriminant is less than zero, it informs the user that there are no real roots.
    """
    print("stanCode Quadratic Solver!")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two real root:")
        print("Root 1:", root1, end="")
        print(" Root 2:", root2, end="")
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One real root:")
        print("Root:", root)
    else:
        print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
