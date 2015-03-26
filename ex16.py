from sys import argv

script, filename = argv

print "We're going to erase %s." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit Enter."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# no need to truncate this file
# because it will be truncated by the open() method with 'w' mode
print "Truncating the file. Goodbye!"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()