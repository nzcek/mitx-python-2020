def getAvailableLetters(lettersGuessed):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	newalpha = alphabet
	for letter in lettersGuessed:
		if letter in lettersGuessed:
			newalpha = newalpha.replace(letter,"")
	print(newalpha)	

	