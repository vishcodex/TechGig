# Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
# You will be given two integers denoting sides AB and BC respectively.
# Round off your answer to the nearest Integer.

# Input Format
# First line will contain an Integer denoting side AB.
# Second line will contain an Integer denoting side BC.

from math import sqrt, acos, degrees

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():

 # Write code here 
    ab = int(input())
    bc = int(input())

    ac = sqrt(pow(ab,2)+pow(bc,2))
    angle = degrees(acos(ab/ac))
    return int(angle)


a = main()

print(a)

