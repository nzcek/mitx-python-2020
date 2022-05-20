def hangman(secretWord):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	lettersGuessed = []
	coolguy = 'your word is %d letters long' % (len(secretWord))
	print(coolguy)
	while 
		print('-----------')

hangman('hello')

def getAvailableLetters(lettersGuessed):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	newalpha = alphabet
	for letter in lettersGuessed:
		if letter in lettersGuessed:
			newalpha = newalpha.replace(letter,"")
	print(newalpha)	

def getGuessedWord(secretWord, lettersGuessed):
	words = secretWord
	for letter in secretWord:
		if letter not in lettersGuessed:
			words = words.replace(letter, " _ ")
	print(words)		
getGuessedWord('orange', ['e'])