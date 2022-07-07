# You just need to take string input from stdin and checks whether all the case-based characters (letters) of the string are uppercase.

# Input Format
# You will be taking a string as an input from stdin.

# Constraints
# 1 <= |S| <= 10000

# Output Format
# You need to print the boolean value(either True or False) to the stdout.

def main():

 # Write code here 
    value = input()

    if value.isupper():
        print(True)
    else:
        print(False)

main()