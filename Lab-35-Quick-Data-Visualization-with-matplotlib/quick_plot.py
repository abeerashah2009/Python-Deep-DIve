import matplotlib
matplotlib.use('Agg')  # no display available: render to a file
import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# Create the line plot
plt.plot(x, y)

# Customize the plot
plt.title('Simple Line Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')

# Save the plot as an image
plt.savefig('plot.png')
print('Saved plot.png')
