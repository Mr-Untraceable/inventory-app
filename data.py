import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Set the random seed for reproducibility
np.random.seed(42)

# Generate input features
X = np.linspace(-10, 10, 100).reshape(-1, 1)

# Generate target labels with some noise
y = 3 * X + 2 + np.random.randn(100, 1)

# Save the data as a CSV file
data = np.concatenate((X, y), axis=1)  # Concatenate X and y horizontally
np.savetxt('data.csv', data, delimiter=',')

# Scatter plot
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.savefig('scatter_plot.png')
plt.close()

# Pie chart
labels = ['Positive', 'Negative']
positive_count = len(y[y > 0])
negative_count = len(y[y < 0])
sizes = [positive_count, negative_count]

fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
fig.update_layout(title='Target Labels Distribution')

fig.write_html('pie_chart.html')

# Print the generated data
print("Input features (X):")
print(X[:5])  # Print the first 5 rows of X
print("\nTarget labels (y):")
print(y[:5])  # Print the first 5 rows of y
