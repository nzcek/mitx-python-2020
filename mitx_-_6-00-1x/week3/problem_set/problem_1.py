def isWordGuessed(secretWord, lettersGuessed):
	letters = secretWord.split()
	for letter in lettersGuessed:
		if letter.all() in letters:
			letters.clear() 
	if len(li) == 0:
		return True
	else:
		return False  

