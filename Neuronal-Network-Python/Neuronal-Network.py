import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#layer = tf.keras.layers.Dense(units="number of neurons in the layer", input_shape=["Input neurons"]) ; Dense = Fully connected layer
#model = tf.keras.Sequential([layer])

hidden1 = tf.keras.layers.Dense(units=3, input_shape=[1])
hidden2 = tf.keras.layers.Dense(units=3)
output = tf.keras.layers.Dense(units=1)
model = tf.keras.Sequential([hidden1, hidden2, output])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'                   # 0.1 = learning rate. Too low, learn slowly. Too high, cant learn correctly.
)

print("Training...")
history = model.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Trained")

plt.xlabel("# Age")
plt.ylabel("Loss")
plt.plot(history.history["loss"])

print("Test 1: 100 ºC")
result = model.predict(np.array([100.0]))
print(str(result) + "f")
print("Test 2: -220.6 ºC")
result = model.predict(np.array([-220.6]))
print(str(result) + "f")
print("Test 3: 5.75896 ºC")
result = model.predict(np.array([5.75896]))
print(str(result) + "f")
