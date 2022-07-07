# Python.math module provides access to the mathematical functions defined by the C standard.
# One of the widely used function is math.pow(x, y) which Returns x raised to the power y.
# Now, you are given three integers x, y and M. You have to print ( x ^ y ) Mod M.

# Input Format
# First line will contain three integers x, y, and M.

# Constraints
# 1 <= X <= 20
# 1 <= Y <= 100
# 2 <= M <= 100

# Output Format
# Print an Integer denoting answer of the calculation (x ^ y ) Mod M.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 

    iput_value = input().split()
    int_values = [ int(x) for x in iput_value ]
    return (int_values[0] ** int_values[1]) % int_values[2]

res = main()

print(res)

