# You just need to take string input from stdin and bunch from strings one on each line and you need to concatenate them as shown in the sample.

# Input Format
# You will be taking strings as an input from stdin one on each line respectively.

# Constraints
# 1 <= |S| <= 10000

# Output Format
# You need to print the string after concatenation to the stdout.

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    l = list()
    special_char = input()
    while True:
        try :
            l.append(input())
        except:
            break
    print(special_char.join(l))

 # Write code here 

main()

