# You just need to take string input from stdin and checks whether the string consists of digits only.

# Input Format
# You will be taking a string as an input from stdin.

# Constraints
# 1 <= |S| <= 10000

# Output Format
# You need to print the boolean value(either True or False) to the stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    value = input()

    if value.isdigit():
        print(True)
    else:
        print(False)

main()

