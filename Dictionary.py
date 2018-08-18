# The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

#Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead). To check whether a single key is in the dictionary, use the in keyword.

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print('jack', tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
list(tel)
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # The dict() constructor builds dictionaries directly from sequences of key-value pairs
tel3 = dict(sape=4139, guido=4127, jack=4098) # When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
print('tel2', tel2)
print('tel3', tel3)
