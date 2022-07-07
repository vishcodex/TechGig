# You just need to take string and a character as an input from stdin and print 'True' if that character is present in that string otherwise print 'False'.

# Input Format
# You will be taking a string and a character as an input from stdin.

# Constraints
# 1 <= |S| <= 10000

# Output Format
# Print 'True' if that character is present in that string otherwise print 'False'.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

from numpy import character


def main():

 # Write code here 
    value = input()
    character = input()

    if character in value:
        print("True")
    else:
        print("False")

main()

