#python learning practice

# functions
def echo(thing):
	return thing
	
def swap(thing1, thing2):
	return thing2, thing1

# arithmetic functions
def reverse(x):
	return -x

def plus(a, b):
	return (a + b)

def main_arithmetic():
	print "reverse(4): ", reverse(4)
	print "sum of (3, 4): ", plus(3, 4)
def main(): 
	print "echo(baseball bat): ", echo("baseball bat")
	print "swap('fame', 'fortune'): ", swap("fame", "fortune")
	print "swap(6, 9): ", swap (6, 9)
	main_arithmetic()
	
	
main()