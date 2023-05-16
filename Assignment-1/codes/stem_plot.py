import matplotlib.pyplot as plt

# Probabilities
same_day_prob = 1/5
consecutive_days_prob = 8/25
different_days_prob = 4/5

# Create stem plot
plt.stem([1], [same_day_prob], basefmt=" ")
plt.stem([2], [consecutive_days_prob], basefmt=" ")
plt.stem([3], [different_days_prob], basefmt=" ")

# Set labels and title
plt.xticks([1, 2, 3], ['Same Day', 'Consecutive Days', 'Different Days'])
plt.ylabel('Probability')
plt.title('Probability Stem Plot')

# Save the plot as a PDF file
plt.savefig('stem_plot.pdf')

# Display the plot
plt.show()

