import random, time
from Fitting import lin, quad, fit
from matplotlib import pyplot as plt

x_axis_data = []

for i in range(0, 500, 20):
    x_axis_data.append(i)

def bubble_sort(L):
    # bubble sort example from the book 
    for i in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]


def time_function(func, args):
    start_time = time.time()
    func(args)

    return time.time() - start_time



y_axis_data = []
for point in x_axis_data:
    L = [random.randint(0, point) for i in range(point)]
    y_axis_data.append(time_function(bubble_sort, L)*1000)



lin_data_points = fit(lin, x_axis_data, y_axis_data)

y_axis_1 = lin_data_points[2]

for data in y_axis_1:
    data *= 1000

quad_data_points = fit(quad, x_axis_data, y_axis_data)

y_axis_2 = quad_data_points[2]

for data in y_axis_2:
    data *= 1000



plt.figure()

plt.scatter(x_axis_data, y_axis_data)

plt.plot(x_axis_data, y_axis_1, label = 'lin_data_points', c="r", marker='*')

plt.plot(x_axis_data, y_axis_2, label = 'quad_data_points', c="b", marker='*')

plt.legend()

plt.savefig('bestfig.png')