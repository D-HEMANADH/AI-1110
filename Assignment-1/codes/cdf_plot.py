import matplotlib.pyplot as plt
import numpy as np

# Define the values of Z and their corresponding probabilities
Z_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
Z_probs = [0.04, 0.08, 0.12, 0.16, 0.2, 0.16, 0.12, 0.08, 0.04]

# Calculate the CDF
Z_cdf = np.cumsum(Z_probs)

# Plot the CDF
plt.plot(Z_values, Z_cdf, drawstyle='steps-post')
plt.xlabel('Z')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Z')
plt.show()

