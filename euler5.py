def problem5():
	returnValue = 1
	numbers = [i for i in range(1,21)]
	#multiply value by all primes
	primes = [2,3,5,7,11,13,17,19]
	for prime in primes:
		returnValue *= prime
	#cover all multiples of 3 and 9 (we've already multiplied by 3)
	returnValue *= 3
	#cover all multiples of 4, 8, 16 (we've already multiplied by 2)
	returnValue *= 8
	return returnValue

