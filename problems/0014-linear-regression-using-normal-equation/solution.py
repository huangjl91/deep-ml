from sklearn.linear_model import LinearRegression
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# 调用线性回归模型做训练
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

	# 接收斜率和截距并四舍五入
    result = []
	for v in model.coef_:
		result.append(round(v, 4))
	return result
