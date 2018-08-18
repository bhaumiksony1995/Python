# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

for i in range(5):
	print(i)

print('')

# It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’)
for i in range(5, 10):
	print(i)

print('')

for i in range(0, 10, 3):
	print(i)

print('')

for i in range(-10, -100, -30):
	print(i)

print('')

# To iterate over the indices of a sequence, you can combine range() and len()
a = ["mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
	print(i, a[i])

print('')

print(list(range(5)))

