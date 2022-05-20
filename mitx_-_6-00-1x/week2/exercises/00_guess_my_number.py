count=0
high=100
low=0
print("Please think of a number between 0 and 100!")
while input != 'c':
newnum=int((high+low)/2)
print("Is your secret number "+str( newnum)+"?")
x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
if x == 'h':
high = newnum
count+=1
elif x == 'l':
low = newnum
count+=1
elif x == 'c':
print("Game over. Your secret number was: " + str( newnum))
break
else: 
print("try again")
