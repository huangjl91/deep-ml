import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	arr = np.array(matrix)
	if mode == 'row':
		result = np.mean(arr, axis = 1)   #行
	else:
		result = np.mean(arr, axis = 0)   #列

	return result.tolist()
		
