# ex15 reading files

# import argv module
from sys import argv

# unpack the argv
script, filename = argv

# open the file
txt = open(filename)

# print the file name
print "Here's your file %s:" % filename
# print the file content
print txt.read()

# reread the file
print "Type the filename again:"
file_again = raw_input("> ")

# reopen the file
txt_again = open(file_again)
# print the file again
print txt_again.read()