from matplotlib import pyplot as plt        # import plotting funcs
from TimeFunctions import  time_function    # import the time function you will write
from Duplicates import has_duplicates_1, has_duplicates_2     # import the has_duplicates functions you are interested in


# All code below is included as a demo. Feel free to change any of it.

##### Initialize datasets
# Pick 3 x-values
x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 100]

##### Measure the running times
# Generate 3 corresponding y-values
y1 = []
for n in x:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y1.append(time_function(has_duplicates_1, L) * 1000) # append running time to y

y2 = []
for n in x:
    L = [i for i in range(n)]
    y2.append(time_function(has_duplicates_2, L) * 1000)

print("y1: ", y1)
print("y2: ", y2)

##### Plot datasets
plt.figure()
plt.scatter(x, y1, c='r', marker='x', label='has_duplicates_1')
plt.scatter(x, y2, c='b', marker='*', label='has_duplicates_2')
plt.ylabel("running time (s)")
plt.xlabel("number of items")
plt.legend()

# plt.show()
plt.savefig('figure_1.png')





