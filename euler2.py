def problem2():
	prev2 = 1
	prev1 = 2
	currentTerm = prev1 + prev2
	i = 2
	evenFibonacciNumbers = []
	evenFibonacciNumbers.append(2)
	while (True):
		currentTerm = prev2 + prev1;
		if (currentTerm > 4000000):
			break
		prev2 = prev1
		prev1 = currentTerm
		i += 1
		if (currentTerm % 2 == 0):
			evenFibonacciNumbers.append(currentTerm)
	return sum(evenFibonacciNumbers)