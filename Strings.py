#Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes ('...') or double quotes ("...") with the same result [2]. \ can be used to escape quotes:

print ('spam eggs')
print ('doesn\'t') # use \' to escape the single quote...
print ("doesn't") # ...or use double quotes instead
print ('"Yes," he said.')
print ("\"Yes,\" he said.")
print ('"Isn\'t," she said.')
print('')
print ('C:\some\name')
print (r'C:\some\name')
print (3 * 'un' + 'ium') # 3 times 'un', followed by 'ium'
print ('py' 'thon') #Two or more string literals next to each other are automatically concatenated.
print('')

prefix = 'py'
print (prefix + 'thon')
print ('')

word = 'python'
print (word[0])
print (word[5])
#Indices may also be negative numbers, to start counting from the right:
print (word[-1]) #last character
print (word[-2]) #second to last character
print (word[-6]) #first character
print('')

#In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
print (word[0:2]) # characters from position 0 (included) to 2 (excluded)
print (word[2:5]) # characters from position 2 (included) to 5 (excluded)
print ('')

#Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
print (word[:2] + word[2:])
print (word[:4] + word[4:])
print ('')

#Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print (word[:2]) # character from the beginning to position 2 (excluded)
print (word[4:]) # characters from position 4 (included) to the end
print (word[-2:]) # characters from the second-last (included) to the end
print('')

#The built in function len() returns the length of a string
print (len(word))
