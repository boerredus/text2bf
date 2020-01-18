#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
	userInput = sys.argv[1]
else:
	userInput = input("Enter your data: ")
f = open("brainfuck.bf", "w")
userInput = list(userInput)
for num in range(len(userInput)):
    f.write("+" * ord(userInput[num]) + " .")
    f.write("-" * ord(userInput[num]))
f.write("+" * ord("\n") + " .")
f.write("-" * ord("\n"))
f.close()