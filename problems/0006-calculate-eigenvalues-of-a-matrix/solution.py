import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	arr = np.array(matrix)
	result1, result2 = np.linalg.eig(arr)
	return result1.tolist()