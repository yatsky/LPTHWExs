tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\nona line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True: # Finally know how to do this trick haha
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,