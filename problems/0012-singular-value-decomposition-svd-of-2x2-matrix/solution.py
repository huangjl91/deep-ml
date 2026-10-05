import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # 构造对称矩阵
    M = A.T @  A

    # 取出对称矩阵的3个元素
    a = M[0][0]
    b = M[0][1]
    c = M[1][1]

    # 用雅可比旋转公式算旋转角度
    if abs(a - c) < 0:
        sita = np.pi / 4
    else:
        sita = 0.5 * np.arctan(2 * b / (a - c))

    # 用sita构造旋转矩阵v
    cos_sita = np.cos(sita)
    sin_sita = np.sin(sita)
    V = np.array([[cos_sita, -sin_sita], [sin_sita, cos_sita]])

    # 对角化M，取特征值
    log_M = V.T @ M @ V

    # 取出两个奇异值s1, s2
    s1 = np.sqrt(log_M[0][0])
    s2 = np.sqrt(log_M[1][1])

    # 奇异值按从小到大排序
    if s1 < s2:
        s1, s2 = s2, s1
        V = V[:, [1, 0]]
    s = np.array([s1, s2])
    vt = V.T

    # 算出左奇异向量U
    U = A @ V @ np.diag([1 / s1, 1 / s2])

    return U, s, vt

