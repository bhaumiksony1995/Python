# open() returns a file object, and is most commonly used with two arguments: open(filename, mode). Mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

f = open('workfile', 'r+')

with open('workfile') as f:
    read_data = f.read()
print(f.closed)
print(read_data)

# f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''

# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
for line in f:
	print(line, end='')

This is the first line of the file.
Second line of the file

# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
# f.write(string) writes the contents of string to the file, returning the number of characters written.
f.write('This is a test\n')
15

# To change the file object’s position, use f.seek(offset, from_what). The position is computed from adding offset to a reference point; the reference point is selected by the from_what argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. from_what can be omitted and defaults to 0, using the beginning of the file as the reference point.
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
