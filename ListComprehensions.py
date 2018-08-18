# List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

#For example we want to create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)

squares2 = list(map(lambda x: x**2, range(10))) # this does the same thing without overwriting x
squares3 = [x**2 for x in range(10)] #also does the same thing

print("squares: ", squares)
print("squares2: ", squares2)
print("squares3: ", squares3)

print('')

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

combs2 = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] # this does the same thing as the for loop above
print(combs2)

print('')

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
vecDoubled = [x*2 for x in vec]
print("vecDoubled", vecDoubled)

print('')

# filter the list to exclude negative numbers
vecNoNegs = [x for x in vec if x >= 0]
print("vecNoNegs", vecNoNegs)

print('')

# apply a function to all the elements
vec2 = [abs(x) for x in vec]
print("vec2", vec2)

print('')

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print(freshfruit)
[weapon.strip() for weapon in freshfruit]

print('')

# create a list of 2-tuples like (number, square)
tuple = [(x, x**2) for x in range(6)]
print(tuple)

print('')

#List comprehensions can be nested
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print('')

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
print('')

transposed2 = [[row[i] for row in matrix] for i in range(4)]
print(transposed2)

#an even shorter way to transpose is to use zip
transposed3 = list(zip(*matrix))
print(transposed3)
