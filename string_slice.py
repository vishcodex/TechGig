# You need to take string input and two other numbers which will be the start and end point of the slice and you need to print that slice of string.

# Input Format
# You will be given a function with string and two other integers as arguments.

# Constraints
# 1 <= |S| <= 10^3

# Output Format
# You need to return the slice of the string.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 word = input()
 start = int(input())
 end = int(input())

 print(word[start:end+1])


main()

