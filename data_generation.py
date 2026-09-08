import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Generate input features
X = np.linspace(-10, 10, 100).reshape(-1, 1)

# Generate target labels with some noise
y = 3 * X + 2 + np.random.randn(100, 1)

# Print the generated data
print("Input features (X):")
print(X[:5])  # Print the first 5 rows of X
print("\nTarget labels (y):")
print(y[:5])  # Print the first 5 rows of y
