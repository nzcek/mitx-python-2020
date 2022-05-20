def isPrime(n):
	if n == 1:
		return False
	
	for i in range(2, n):
		if (n % i) == 0:
			return False
	return True

def genPrimes():
	primes = [2]
	x = 2
	while True:
		if isPrime(x):
			primes.append(x)
			yield x	
		x += 1


