# Python has functions for creating, reading, updating, and deleting files.

# Open/create a file
myFile = open('myfile.txt', 'w')

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I am also like NodeJS')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)

# Get some info
print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)