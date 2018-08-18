# We can create a function that writes the Fibonacci series to an arbitrary boundary

def fib(n):
	"""Print a Fibonacci sequence up to n"""
	a, b = 0, 1
	while a < n:
		print (a, end=', ')
		a, b = b, a+b
	print()

# Now call the function we just defined:
fib(2000)

def fib2(n):
	"""Return a list containing the Fibonacci series up to n."""
	results = []
	a, b = 0, 1
	while a < n:
		results.append(a)
		a, b = b, a+b
	return results

print(fib2(2000))
