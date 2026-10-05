import numpy as np
def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# 将proint 和 centroids变成矩阵后面做运算
	points = np.array(points)
	centroids = np.array(initial_centroids)

	# 每个点分配给最近的重心
	for i in range(max_iterations):
		clusters = []   # 用来保存点所在簇的序号

		# 算颠倒中心的距离
		for point in points:
			distance = []
			for c in centroids:
				d = np.linalg.norm(point - c)
				distance.append(d)
			clusters.append(np.argmin(distance))  # 找距离最小的值

		clusters = np.array(clusters)

		# 重新取平均值计算每个簇的重心
		new_centroids = []
		for i in range(k):
			new_points = points[clusters == i]
			if len(new_points) > 0:
				new_centroids.append(new_points.mean(axis = 0))  # 算出新的点的重心放入新的簇中
			else:
				new_centroids.append(centroids[i])  # 空簇保持不变
		
		centroids = np.array(new_centroids)
		# 用result来接收结果
	result = []
	for c in centroids:
		result.append(tuple(np.round(c, 4)))
	return result