# The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow.

def ask_ok(prompt, retries=4, reminder="Please try again!"):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		elif ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if returies < 0:
			raise ValueError('Invalid user response')
		print(reminder)

# This function can be called in several ways:
ask_ok('Do you really want to quit?') # giving only the mandatory argument
ask_ok('OK to overwrite the file?', 2) # giving one of the optional arguments
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!') # or even giving all arguments

# The default values are evaluated at the point of function definition in the defining scope, the following function will print 5 not 6
i = 5
def f(arg=i):
	print(arg)
i = 6
f()

print('')

# The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print('')

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f2(1))
print(f2(2))
print(f2(3))
