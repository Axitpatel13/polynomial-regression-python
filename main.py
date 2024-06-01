import matplotlib.pyplot as plt
import numpy as np
# Sample data (temperature, lemonades sold)
temp = np.array([10, 15, 20, 25, 30])
sales = np.array([20, 30, 40, 50, 35])
# Fit a linear regression (degree 1)
plt.plot(temp, sales, 'o', label='Data')  # Plot data points
m, b = np.polyfit(temp, sales, 1)  # Fit linear regression
plt.plot(temp, m * temp + b, label='Linear Regression')
# Fit a second-degree polynomial regression
m2, b2, c2 = np.polyfit(temp, sales, 2)  # Fit polynomial regression
plt.plot(temp, m2 * temp**2 + b2 * temp + c2, label='Polynomial Regression')
plt.xlabel('Temperature (°C)')
plt.ylabel('Lemonades Sold')
plt.legend()
plt.grid(True)
plt.show()
