import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))
	D = np.diag(np.diag(A))
	D_inv = np.linalg.inv(D)
	R = A - D

	for i in range(n):
		x = D_inv @ (b - R @ x)
	
	result = []
	for v in x:
		result.append(round(v, 4))
	return result