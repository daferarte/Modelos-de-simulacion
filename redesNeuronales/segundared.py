import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler

# cargar el dataset
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# Normalizar caracteristicas (Muy importante en Redes Neuronales)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

# constuir modelo de la red neuronal
model = Sequential([
    Dense(64, activation="relu", input_shape=(x_train.shape[1],)),
    Dense(64, activation="relu"),
    Dense(1) # una sola salida porque es regresion
])

# Compilar modelo
model.compile(optimizer='adam',
              loss='mse', #error cuadratico medio
              metrics=['mae']) # error absoluto medio

# entrenar el modelo
model.fit(x_train, y_train,
          epochs=100,
          batch_size=16,
          validation_split=0.2,
          verbose=1)

# evaluar el modelo
loss, mae = model.evaluate(x_test, y_test)
print(f'Error absoluto medio (MAE): {mae:.2f}')
