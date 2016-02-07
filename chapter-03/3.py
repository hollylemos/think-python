#Problem 1:
#Python provides a built-in function called len that returns the length of a string
#so the value of len('allen') is 5. 
#Write a function named right_justify that takes a string named s as a parameter and prints
#the string with enough leading spaces so that the last letter of the string is in column 70
#of the display.

#word = raw_input('Type a word to send over there ---->\n')

def right_justify(word):
	print " " * (70 - len(word)) + word

#right_justify(word)



#Problem 2:


#1. Type this example into a script and test it:
#def do_twice(f): 
#f()
#f()

#2. Modify do_twice so that it takes two arguments, a function object and a value, 
#and calls the function twice, passing the value as an argument.
#3. Write a more general version of print_spam, called print_twice, that takes a 
#string as a parameter and prints it twice.
#4. Use the modified version of do_twice to call print_twice twice, passing 'spam' 
#as an argument.
#5. Define a new function called do_four that takes a function object and a value 
#and calls the function four times, passing the value as a parameter. There should 
#be only two statements in the body of this function, not four.


word = raw_input('Type a word to repeat\n')

string = raw_input('Type something here\n')

def do_twice(f, word):
	print_twice('spam')
	print_twice('spam')

def print_spam(word):
	print word

def print_twice(string):
	print string
	print string

def do_four(f, word):
	do_twice(string, word)
	do_twice(string, word)
	

do_four(print_twice, 'spam')
print ''