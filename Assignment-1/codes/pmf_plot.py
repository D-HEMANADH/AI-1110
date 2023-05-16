import matplotlib.pyplot as plt
# Define the values of Z and their corresponding probabilities
Z_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
Z_probs = [0.04, 0.08, 0.12, 0.16, 0.2, 0.16, 0.12, 0.08, 0.04]

# Plot the PMF
plt.bar(Z_values, Z_probs)
plt.xlabel('Z')
plt.ylabel('Probability')
plt.title('PMF of Z')
plt.savefig("../figs/pmf_plot.pdf")
plt.show()

