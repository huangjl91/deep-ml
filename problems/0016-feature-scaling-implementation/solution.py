import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# 标准化：(x - 均值) / 标准差
	mean = np.mean(data, axis = 0)
	std = np.std(data, axis = 0)
	standardized_data = (data - mean) / std

	# 归一化：(x - 最小值) / (最大值 - 最小值)
	min_data = np.min(data, axis = 0)
	max_data = np.max(data, axis = 0)
	normalized_data = (data - min_data) / (max_data - min_data)
	
	return standardized_data, normalized_data