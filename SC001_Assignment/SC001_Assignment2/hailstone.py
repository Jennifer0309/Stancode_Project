"""
File: hailstone.py
Name: Jennifer Li
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Allow the user to input any integer and generate the Hailstone Sequence.
    All numbers before reaching 1 will be listed.
    Additionally, the number of operations (steps) from n to 1 in this sequence will be recorded.
    If the user directly inputs 1 after recompiling, the program will show 0 steps.
    Choose a positive integer n and repeat the following instructions until n becomes 1:
    If n is odd, multiply n by 3 and add 1.
    If n is even, divide n by 2.
    """
    print("This program computes Hailstone sequences")
    print("")
    hailstone()


def hailstone():
    n = int(input("Enter a number:"))  # Prompt the user to enter a number
    steps = 0  # Initialize the step counter
    while n != 1:  # Continue the loop until n becomes 1
        old_n = n
        if n % 2 == 1:  # Check if n is odd
            n = n * 3 + 1
            print(str(old_n) + ' is odd,so I make 3n+1:' + str(n))
        else:
            # n % 2 == 0  # Check if n is even
            n = n // 2
            print(str(old_n) + ' is Even,so I take half:' + str(n))
        steps += 1  # Increment the step counter
    print("It took", steps, "to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
