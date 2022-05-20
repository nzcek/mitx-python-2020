def getGuessedWord(secretWord, lettersGuessed):
	words = secretWord
	for letter in secretWord:
		if letter not in lettersGuessed:
			words = words.replace(letter, " _ ")
	print(words)		
getGuessedWord('orange', ['e'])