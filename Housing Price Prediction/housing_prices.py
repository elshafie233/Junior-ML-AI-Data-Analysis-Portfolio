import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

m = 200

size = np.random.randint(600, 3500, size=m)
bedrooms = np.random.randint(1, 6, size=m)
age = np.random.randint(0, 40, size=m)
distance = np.random.randint(1, 30, size=m)

# Feature engineering
size_Square = size ** 2
size_per_bedroom = size / bedrooms
house_age_squared = age ** 2

price = (
    50000
    + 150 * size
    + 10000 * bedrooms
    - 1200 * age
    - 2000 * distance
    + np.random.normal(0, 20000, m)
)

data = pd.DataFrame(
    {
        "size": size,
        "bedrooms": bedrooms,
        "age": age,
        "distance": distance,
        "size_squared": size_Square,
        "size_per_bedroom": size_per_bedroom,
        "house_age_squared": house_age_squared,
        "price": price,
    }
)

data["price"] = data["price"].round(2)

print(data.head())


def normalize_features(X):
    normalized_X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    return normalized_X


def predict(X, w, b):
    f_wb = np.dot(X, w) + b
    return f_wb


def compute_cost(X, y, w, b):
    m = X.shape[0]
    cost = (1 / (2 * m)) * np.sum((predict(X, w, b) - y) ** 2)
    return cost


def compute_gradient(X, y, w, b):
    m = X.shape[0]
    dj_dw = (1 / m) * np.dot(X.T, (predict(X, w, b) - y))
    dj_db = (1 / m) * np.sum(predict(X, w, b) - y)
    return dj_dw, dj_db


def gradient_descent(X, y, w, b, alpha, iterations):
    cost_history = []

    for i in range(iterations):
        dj_dw, dj_db = compute_gradient(X, y, w, b)

        w -= alpha * dj_dw
        b -= alpha * dj_db

        cost = compute_cost(X, y, w, b)
        cost_history.append(cost)

    return w, b, cost_history


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)


def logistic_regression(X, y, w, b, alpha, iterations):
    cost_history = []

    for i in range(iterations):
        z = np.dot(X, w) + b
        predictions = sigmoid(z)

        error = predictions - y
        dj_dw = (1 / X.shape[0]) * np.dot(X.T, error)
        dj_db = (1 / X.shape[0]) * np.sum(error)

        w -= alpha * dj_dw
        b -= alpha * dj_db

        # Recalculate predictions after updating parameters
        predictions = sigmoid(np.dot(X, w) + b)

        # Prevent log(0)
        predictions = np.clip(predictions, 1e-15, 1 - 1e-15)

        cost = -np.mean(
            y * np.log(predictions)
            + (1 - y) * np.log(1 - predictions)
        )
        cost_history.append(cost)

    return w, b, cost_history


def regularization(X, y, w, b, alpha, iterations, lambda_):
    cost_history = []

    for i in range(iterations):
        dj_dw, dj_db = compute_gradient(X, y, w, b)

        # Apply L2 regularization
        dj_dw += (lambda_ / X.shape[0]) * w

        w -= alpha * dj_dw
        b -= alpha * dj_db

        cost = compute_cost(X, y, w, b) + (
            lambda_ / (2 * X.shape[0])
        ) * np.sum(w ** 2)

        cost_history.append(cost)

    return w, b, cost_history


def dessicion_boundary(X, w, b):
    x1 = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
    x2 = -(w[0] * x1 + b) / w[1]
    return x1, x2


# ==================================
# Training the models
# ==================================

X = data[
    [
        "size",
        "bedrooms",
        "age",
        "distance",
        "size_squared",
        "size_per_bedroom",
        "house_age_squared",
    ]
].values

# Separate targets
y_linear = data["price"].values
y_logistic = (data["price"] >= 350000).astype(int).values

X_normalized = normalize_features(X)

# Training settings
alpha = 0.01
iterations = 1000

# ==================================
# Linear Regression
# ==================================

w = np.zeros(X.shape[1])
b = 0.0

w, b, cost_history = gradient_descent(
    X_normalized, y_linear, w, b, alpha, iterations
)

# ==================================
# Logistic Regression
# ==================================

logistic_w = np.zeros(X.shape[1])
logistic_b = 0.0

logistic_w, logistic_b, logistic_cost_history = logistic_regression(
    X_normalized,
    y_logistic,
    logistic_w,
    logistic_b,
    alpha,
    iterations
)

# ==================================
# Regularized Linear Regression
# ==================================

regularized_w = np.zeros(X.shape[1])
regularized_b = 0.0

regularized_w, regularized_b, regularized_cost_history = regularization(
    X_normalized,
    y_linear,
    regularized_w,
    regularized_b,
    alpha,
    iterations,
    lambda_=0.1
)

# ==================================
# Decision Boundary (2 features)
# ==================================

X_two_features = X_normalized[:, :2]

boundary_w = np.zeros(X_two_features.shape[1])
boundary_b = 0.0

boundary_w, boundary_b, boundary_cost_history = logistic_regression(
    X_two_features,
    y_logistic,
    boundary_w,
    boundary_b,
    alpha,
    iterations
)

dession_x1, dessicion_x2 = dessicion_boundary(
    X_two_features, boundary_w, boundary_b
)

# ==================================
# Display results
# ==================================

print("Weights:", w)
print("Bias:", b)
print("Final Cost:", compute_cost(X_normalized, y_linear, w, b))

print("Logistic Weights:", logistic_w)
print("Logistic Bias:", logistic_b)
print("Logistic Final Cost:", logistic_cost_history[-1])

print("Regularized Weights:", regularized_w)
print("Regularized Bias:", regularized_b)
print("Regularized Final Cost:", regularized_cost_history[-1])


# ==================================
# Gradient Descent Learning Curve
# ==================================

plt.figure(figsize=(10, 6))

plt.plot(
    range(1, len(cost_history) + 1),
    cost_history,
    color="blue",
    linewidth=2,
    label="Training Cost"
)

plt.xlabel("Iterations")
plt.ylabel("Cost J(w,b)")
plt.title("Gradient Descent Learning Curve")

plt.legend()
plt.grid(True)
plt.savefig("gradient_descent_curve.png")
plt.show()
