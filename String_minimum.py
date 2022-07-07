# You just need to take string input from STDIN and print the min alphabetical character from the string.

# Input Format
# You will be taking a string as an input from STDIN. 

# Constraints
# 1 <= |S| <= 10000

# Output Format
# You need to print the min alphabetical character from the string to the STDOUT. 

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(): 
    x=input()
    x=x.replace(" ","")
    if not x.isupper(): 
        x=x.lower() 
        print(min(x))
    else: 
        print(min(x))

main()

