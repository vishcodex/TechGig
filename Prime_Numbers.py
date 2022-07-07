# You just need to take two number as input from stdin and you need to find prime numbers between those two numbers and print them.

# Input Format
# You will be taking two numbers as an input from stdin one on each line respectively.

# Constraints
# 1 <= N <= 10000

# Output Format
# You need to print the prime numbers one on each line to the stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    print("Please enter lowest number")
    a = int(input())
    print("Please enter highest number") 
    b = int(input())

    # Logic for finding prime number

    for num in range (a, b):  
        if num > 1:  
            for i in range (2, num):  
                if (num % i) == 0:  
                    break  
            else:  
                print (num) 

main()