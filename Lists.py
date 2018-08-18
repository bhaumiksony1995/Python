# Can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

squares = [1, 4, 9, 16, 25]
print ("squares[1, 4, 9, 16, 25]")
print (squares)
print('')

#Like strings (and all other built-in sequence type), lists can be indexed and sliced:
print ("squares[0]")
print (squares[0]) # indexing returns the item
print('')

print("squares[-1]")
print(squares[-1])
print('')

print("squares[-3:]") # slicing returns a new list
print(squares[-3:]) 
print('')

print("squares[:]") # All slice operations return a new list containing the requested elements. The following slice returns a new (shallow) copy of the list
print(squares[:])
print('')

# Lists also support operations like concatenation:
print("squares + [36, 49, 64, 81, 100]")
print(squares + [36, 49, 64, 81, 100])
print('')

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]
print("cubes = [1, 8, 27, 65, 125]") #the cube of 4 is 64 not 65, lets change that
print (cubes)
cubes[3] = 64
print("cubes[3] = 64")
print(cubes) #The cube of 4 is now 64 not 65
print('')

# You can also add new items at the end of the list, by using the append()
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print("cubes.append(216)")
print("cubes.append(7 ** 3)")
print(cubes)
print('')

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']")
letters[2:5] = ['C', 'D', 'E'] # replace some values
print("letters[2:5] = ['C', 'D', 'E']")
print(letters)
letters[2:5] = [] # now remove them
print("letters[2:5] = []")
print(letters)
letters[:] = [] # clear the list by replacing all the elements with an empty list
print("letters[:] = []")
print(letters)
print('')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("len(alphabet)")
print(len(alphabet))
print('')

# It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print("a = ['a', 'b', 'c']")
print("n = [1, 2, 3]")
print("x = [a, n]")
print(x)
print("x[0]")
print(x[0])
print("x[0][1]")
print(x[0][1])
print('')

#All the methods for list
#list.append(x) # Add an item to the end of the list
#list.extend(iterable) # Extend the list by appending all the items from the iterable
#list.insert(x) # Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the 
	       # front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#list.remove(x) # Remove the first item from the list whose value is equal to x. It is an error if there is no such item.
#list.pop([i]) # Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the 
	      # list. (The square brackets around the i in the method signature denote that the parameter is optional
#list.clear() # Remove all items from the list
#list.index(x[,start[, end]]) # Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#list.count(x) # Return the number of times x appears in the list.
#list.sort(key=None, reverse=False) # Sort the items of the list in place 
#list.reverse() # Reverse the elements of the list in place.
#list.copy() # Return a shallow copy of the list

###Examples of most of the list methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print("apple ", fruits.count('apple'))
print("tangerine ", fruits.count('tangerine'))
print("banana ", fruits.index('banana'))
print("next banana ", fruits.index('banana', 4))  # Find next banana starting a position 4
print(fruits.reverse())
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

print('')

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del(a[0])
print("del a[0] ", a)
del(a[2:4])
print("del a[2:4] ", a)
del(a[:])
print("del(a[:]) ", a)
