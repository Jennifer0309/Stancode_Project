"""
File: prime_checker.py
Name: Jennifer Li
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
SECRET = -100


def main():
    """
    Write a program that allows the user to repeatedly enter numbers
    and determine whether each number is a prime number.
    """
    print("Welcome to the prime checker!")
    while True:
        n = int(input("n: "))
        # Check if the user has entered the SECRET code to exit
        if n == SECRET:
            print("Have a good one!")
            break
        # Check if the number is 1, which is not considered a prime number
        elif n == 1:
            print(n, "is not a prime number")
        # Check if the number is greater than 1
        elif n > 1:
            # Loop through all numbers from 2 to n-1 to check for factors
            for i in range(2, n):  # If n is divisible by i, it's not a prime number
                if n % i == 0:
                    print(n, "is not a prime number")
                    break
            else:
                # If the loop completes without finding any factors, n is prime
                print(n, "is a prime number")
        # Handle cases where the input is less than or equal to 0
        # else:
        #     print(n, "is not a prime number")
        elif n == 0:
            print(n, "is not a prime number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
