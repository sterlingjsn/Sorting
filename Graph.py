import csv
import numpy as np
import matplotlib.pyplot as plt

with open('results.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = np.array(data)
x_axis = data[1:, 0]

y_bubble = data[1:, 1]
y_insertion = data[1:, 2]
y_quick = data[1:, 3]
y_tim = data[1:, 4]

plt.xlabel("List Length")
plt.ylabel("Performance Time")
plt.plot(x_axis, y_bubble, label="Bubble Sort")
plt.plot(x_axis, y_insertion, label="Insertion Sort")
plt.plot(x_axis, y_quick, label="Quick Sort")
plt.plot(x_axis, y_tim, label="Tim Sort")
plt.legend()

plt.yscale("log")
plt.xscale("log")
plt.show()
