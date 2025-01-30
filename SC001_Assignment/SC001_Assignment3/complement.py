"""
File: complement.py
Name: Jennifer Li
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program will use string manipulation
    to find the complement strand of given DNA sequences  .
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(D):
    """
    :param dna: str, the template used to make a complement ssDNA sequence.
    :return ans: str, the complement ssDNA sequence.
    """
    ans = ''
    if len(D) == '':
        # check before for loop
        return 'DNA strand is missing'
    for i in range(len(D)):

        if D[i] == 'A':
            ans += 'T'
        elif D[i] == 'T':
            ans += 'A'
        elif D[i] == 'C':
            ans += 'G'
        elif D[i] == 'G':
            ans += 'C'
        else:
            pass
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
