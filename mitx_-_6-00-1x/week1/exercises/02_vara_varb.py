if str in (type(varA), type(varB)):
	print("string involved")
elif (type(varA) == int and type(varB) == int): 
	if (varA == varB): 
		print("equal") 
	elif (varA > varB): 
		print("bigger") 
	elif (varA < varB): 
		print("smaller")