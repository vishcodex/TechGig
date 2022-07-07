# You just need to take two numbers as input from stdin and you need to subtract the one from later.

# Input Format
# You will be taking two numbers as an input from stdin one on each line respectively.

# Constraints
# 1 <= N <= 10000

# Output Format
# You need to print the output of the subtraction to stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
 # Write code here 
    a = int(input())
    b = int(input())
    return abs(a-b)

a = main()
print(a)

