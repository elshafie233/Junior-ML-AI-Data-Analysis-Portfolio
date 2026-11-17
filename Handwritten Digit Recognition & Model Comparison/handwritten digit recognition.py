import numpy as np
import tensorflow as tf  # pyright: ignore[reportMissingModuleSource]
from tensorflow.keras.models import Sequential  # pyright: ignore[reportMissingModuleSource]
from tensorflow.keras.layers import Dense, Flatten, Input, Dropout  # pyright: ignore[reportMissingModuleSource]
from tensorflow.keras.losses import SparseCategoricalCrossentropy  # pyright: ignore[reportMissingModuleSource]
from tensorflow.keras.optimizers import Adam  # pyright: ignore[reportMissingModuleSource]

# ==========================================
# 1. Load MNIST Dataset
# ==========================================

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train[0])

# Normalize images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# ==========================================
# 2. Build Neural Network
# ==========================================

model = Sequential([
    Input(shape=(28, 28)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),  # Second Hidden Layer
    Dropout(0.2),
    Dense(10, activation="linear")
])

# ==========================================
# 3. Loss Function & Optimizer
# ==========================================

loss_fn = SparseCategoricalCrossentropy(from_logits=True)

# Example: Loss when correct-class probability = 0.1
loss_value = -tf.math.log(1 / 10)
print("Example Loss:", loss_value.numpy())

optimizer = Adam(learning_rate=0.001)

# ==========================================
# 4. Compile Model
# ==========================================

print("Compiling model...")

model.compile(
    optimizer=optimizer,
    loss=loss_fn,
    metrics=["accuracy"]
)

# ==========================================
# 5. Train Model
# ==========================================

print("Fitting model...")

history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_split=0.2
)

# ==========================================
# 6. Evaluate Model
# ==========================================

print("Evaluate on test data")

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test
)

print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

# ==========================================
# 7. Predict First Test Image
# ==========================================

logits = model(x_test[:1], training=False)

probabilities = tf.nn.softmax(logits, axis=1)

print("Probabilities:", probabilities.numpy())
print(
    "Predicted Digit:",
    tf.argmax(probabilities, axis=1).numpy()
)
print("Actual Digit:", y_test[:1])

# ==========================================
# 8. NumPy Forward Propagation
# ==========================================

def forward_propagation_numpy(x, weights, biases):
    a = x

    for w, b in zip(weights[:-1], biases[:-1]):
        z = np.dot(a, w) + b
        a = np.maximum(0, z)

    z = np.dot(a, weights[-1]) + biases[-1]
    return z

# ==========================================
# 9. Extract Weights and Biases
# ==========================================

weights = []
biases = []

for layer in model.layers:
    if isinstance(layer, tf.keras.layers.Dense):
        w, b = layer.get_weights()
        weights.append(w)
        biases.append(b)

# ==========================================
# 10. Prepare Test Image
# ==========================================

x = x_test[:1]
x_flat = x.reshape(1, 784)

# ==========================================
# 11. NumPy Forward Propagation
# ==========================================

numpy_output = forward_propagation_numpy(
    x_flat,
    weights,
    biases
)

# ==========================================
# 12. TensorFlow Forward Propagation
# ==========================================

tensorflow_output = model(
    x,
    training=False
).numpy()

# ==========================================
# 13. Compare NumPy vs TensorFlow
# ==========================================

print("NumPy Output:", numpy_output)
print("TensorFlow Output:", tensorflow_output)

print(
    "Match:",
    np.allclose(
        numpy_output,
        tensorflow_output,
        rtol=1e-5,
        atol=1e-5
    )
)
