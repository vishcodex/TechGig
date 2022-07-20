# You just need to take three number as input from stdin and you need to find greatest of them.

# Input Format
# You will be taking three numbers as an input from stdin one on each line respectively.

# Constraints
# -100000 <= N <= 100000

# Output Format
# You need to print the greatest of the three numbers to the stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
 v1 = int(input())
 v2 = int(input())
 v3 = int(input())

 arr = [v1,v2,v3]

 print(max(arr))

main()