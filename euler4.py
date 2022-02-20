def problem4():
	maxValue = -1
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			prod = i * j
			if prod > maxValue and isPalindrome(str(prod)):
				maxValue = prod
	return maxValue

def isPalindrome(num):
	numDigits = len(num)
	leftIndex = 0
	rightIndex = numDigits - 1
	while (leftIndex < rightIndex):
		if (num[rightIndex] != num[leftIndex]):
			return False
		leftIndex += 1
		rightIndex -= 1
	return True
