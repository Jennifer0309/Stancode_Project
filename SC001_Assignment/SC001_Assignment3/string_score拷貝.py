"""
File: string_score.py
Name: jennifer Li
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    Tests the score function with different inputs.
    """
    score('1aB4rC')  # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    """
    Calculates the score of a string based on character types.

    :param string: str, the input string to evaluate
    """
    total_score = 0
    for char in string:
        if char.isdigit():  # Check if the character is a digit
            total_score += 1
        elif char.isupper():  # Check if the character is an uppercase letter
            total_score += 2
        elif char.islower():  # Check if the character is a lowercase letter
            total_score += 3
    print(total_score)


if __name__ == '__main__':
    main()
