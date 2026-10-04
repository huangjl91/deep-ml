import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	arr = np.array(vectors)
	result = np.cov(arr)
	return result.tolist()