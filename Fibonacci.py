# we can write an initial sub-sequence of the Fibonacci series as follows:

a, b = 0, 1
while a < 1000:
	print (a)
	a, b = b, a+b

print('')

c, d = 0, 1
while c < 1000:
	print (c, end=', ')
	c, d = d, c+d
