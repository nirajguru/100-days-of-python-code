import sys
print(sys.argv[0])  # this will print argparsing.py
print(sys.argv)  # prints the args as a list comma separated

filename = "niraj.txt"
with open(filename, 'w') as f:
    f.write("hey")
