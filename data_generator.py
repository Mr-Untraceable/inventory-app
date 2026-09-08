import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Set the random seed for reproducibility
np.random.seed(42)

# Generate input features
X = np.linspace(-10, 10, 100).reshape(-1, 1)

# Generate target labels with some noise
y = 3 * X + 2 + np.random.randn(100, 1)

# Scatter plot using matplotlib
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.savefig('scatter_plot.png')
plt.close()

# Histogram using matplotlib
plt.hist(y, bins=20)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.savefig('histogram.png')
plt.close()

# Line plot using matplotlib
plt.plot(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Line Plot')
plt.savefig('line_plot.png')
plt.close()

# Box plot using seaborn
sns.boxplot(y=y.flatten())
plt.ylabel('Values')
plt.title('Box Plot')
plt.savefig('box_plot.png')
plt.close()

# Bar plot using seaborn
labels = ['Positive', 'Negative']
counts = [len(y[y > 0]), len(y[y < 0])]
sns.barplot(x=labels, y=counts)
plt.xlabel('Labels')
plt.ylabel('Counts')
plt.title('Bar Plot')
plt.savefig('bar_plot.png')
plt.close()

# Pie chart using plotly
labels = ['Positive', 'Negative']
sizes = [len(y[y > 0]), len(y[y < 0])]
fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
fig.update_layout(title='Pie Chart')
fig.write_image('pie_chart.png')
fig.write_html('pie_chart.html')

# 3D surface plot using plotly
fig = go.Figure(data=[go.Surface(x=X.flatten(), y=y.flatten())])
fig.update_layout(title='3D Surface Plot')
fig.write_image('surface_plot.png')
fig.write_html('surface_plot.html')

# Heatmap using seaborn
correlation_matrix = np.corrcoef(X.flatten(), y.flatten())
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.savefig('heatmap.png')
plt.close()

