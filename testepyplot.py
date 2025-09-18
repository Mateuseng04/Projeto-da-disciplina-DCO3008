import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

plt.plot(x, y)

plt.title("Sine Wave")

plt.xlabel("X-axis")

plt.ylabel("Y-axis")

plt.show()