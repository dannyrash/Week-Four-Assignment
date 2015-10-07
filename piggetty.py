#
# CIS-125
#
# author_'Danny Rash'
#
# Collab w/ Kollin & Sam
# Collab w/ Devin for help with correct Pig Latin translation
#
# This program translates an English line in a file into Pig Latin
# and writes it to a new file
#
# Define a function called piggy(string) that returns a string

def piggy(word):
	vowels = "aeiouAEIOU"
	d = 0
	lastword = ""
	pig = ""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			if d == 0:
				# True?  We are done
					pig = word + "yay"
			else:
					pig = word[d:] + lastword + "ay"
			break
		else:
			# False? Consonant
			lastword = lastword + letter
			d = d + 1
	return pig

# Open the file *getty.txt* for reading.
infile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.
outfile = open("piggy.txt", "w")

# Read the getty.txt file into a string.
gettystring = infile.read()

# Strip out bad characters (, - .).
gettystring = gettystring.replace("-","")
gettystring = gettystring.replace(",","")
gettystring = gettystring.replace(".","")
	
# Split the string into a list of words.
gettylist = gettystring.split()

# Create a new empty string.
pigified = ""

# Loop through the list of words, pigifying each one.
# Add the pigified word (and a space) to the new string.
for word in gettylist:
	pigified = pigified + piggy(word) + " "

# Write the new string to piggy.txt.  
outfile.write(pigified)

# close the files.
infile.close()
outfile.close()