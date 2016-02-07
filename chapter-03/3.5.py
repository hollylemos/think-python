



def do_twice(x):
	x()
	x()

def do_four(x):
	do_twice(x)
	do_twice(x)

def print_top():
	print '+ - - - - ',

def print_outer_left_post():
	print '|         ',

def print_outers_plus():
	do_twice(print_top)
	print '+'

def print_middle_post():
	do_twice(print_outer_left_post)
	print '|'

def print_row():
	print_outers_plus()
	do_four(print_middle_post)

def print_grid():
	do_twice(print_row)
	print_outers_plus()

print_grid()



