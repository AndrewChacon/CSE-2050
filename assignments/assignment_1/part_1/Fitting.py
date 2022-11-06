import math
from scipy import optimize


def lin(x, m, b):
    return m * x + b

def const(c):
    return c

def quad(x, m, b, c):
    return m * (x ** 2) + b * x + c


def fit_data(f, x_data, y_data):
    params, params_cov = optimize.curve_fit(f, x_data, y_data)

    fit_data_y = [f(x_data[i], * params)for i in range(len(x_data))]
    res = 0

    for data in range(len(x_data)):
        res += ((fit_data_y[data] - y_data[data]) ** 2)

    res = math.sqrt(res/len(x_data))

    return params, res, fit_data_y

x_data_points = []

y_data_points = []

for data in range(20):
    x_data_points.append(data)

for data in range(20):
    y_data_points.append(data)

print((fit_data(quad, x_data_points, y_data_points)))
