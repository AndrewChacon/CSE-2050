from spicy import optimize
# params, params_cov = optimize.curve_fit(func, xdata, ydata) 
from matplotlib import pyplot as plt
# linear fitting function
# the first parameter of a fitting funciton must be x
# subsequent parameters are automatically adjusted by curve_fit
def lin(x, m, b):
 return m * x + b
# generate data on y = 1*x + 0, then add some "noise"
xdata = [i for i in range(10)]
ydata = [i for i in range(10)]
ydata[1] = 2
ydata[8] = 7
# Find parameters for lin that best fit xdata and ydata
params, params_cov = optimize.curve_fit(lin, xdata, ydata)
# unpack the calculated parameters
m = params[0]
b = params[1]
# create an empty list for the line of best fit
y_fit = []
for x in xdata:
    y_fit.append(lin(x, m, b))

# plot the raw data and the line of best fit
plt.figure()
plt.scatter(xdata, ydata)
plt.plot(xdata, y_fit)
plt.show()