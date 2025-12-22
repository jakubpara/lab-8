import matplotlib.pyplot as plt

time = [1, 2, 3, 4, 5,6,7]
speed = [2, 4, 6, 8, 10,13,19]

plt.scatter(time, speed)

plt.xlabel('time')
plt.ylabel('speed')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
