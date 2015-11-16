pyg = "ay"

original = raw_input("Enter a word:")

if len(original) > 0 and orginal.isalpha():
	word = original.lower()
	first = original[0]
	
	if first == "a" or first == "e" or first == "i" or 
	first == "u":
		new_word = word[1:len(word)] + first + pyg
		print new_word
	else:
		print "consonant"

else:
	print "empty"
 
