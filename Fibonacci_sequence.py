# You just need to take a number as input from stdin which will tell how many terms of the Fibonacci needs to be printed.

# Input Format
# You will be taking a number as an input from stdin.

# Constraints
# 1 <= N <= 10000

# Output Format
# You need to print the Fibonacci series separated by space to the stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def fibo(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    

def main():
 # Write code here 
    val = int(input())
    for i in range(val):
        if val < 0:
            print("please enter the correct value")
        else:
            if i == val:
                print(fibo(i),end=' ')
            else:
                print(fibo(i),end=' ')

    # j = 0
    # for i in range(val):
    #     j = j + i
    #     print(j)

main()


