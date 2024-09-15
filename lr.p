import matplotlib.pyplot as plt
import statistics as m
 
x = [1, 2, 4, 3]
y = [5, 6, 7, 2] 
mean_x = m.mean(x)
mean_y = m.mean(y)
n = len(x)

numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
denominator = sum((x[i] - mean_x)**2 for i in range(n))
a1 = numerator / denominator

a0 = mean_y - a1 * mean_x 
o = [a0 + a1 * xi for xi in x]

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, o, color='red', label='Regression Line')
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
plt.legend()
plt.show()
