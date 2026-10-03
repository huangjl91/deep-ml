def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass
	if a == []:
		return []
	m = len(a[0])
	if len(b) != m:
		return -1
	for row in a:
		if len(row) != m:
			return -1
	
	result = []
	for row in a:
		sum = 0
		for i in range(len(row)):
			sum = sum + row[i] * b[i]
		result.append(sum)
	return result

