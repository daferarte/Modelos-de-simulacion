import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar y preparar datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28*28)/255.0
x_test = x_test.reshape(-1, 28*28)/255.0
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Crear modelo
modelo = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

# Compilar 

modelo.compile(optimizer="adam", 
               loss="categorical_crossentropy",
               metrics=['accuracy'])

# Entrenar
modelo.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.1)

# Evaluar
loss, accuracy = modelo.evaluate(x_test, y_test)
print(f'Precision: {accuracy: .2f}')
print(f'loss: {loss: .2f}')

# Precision:  0.98
# Precision:  0.13

# Precision:  0.98
# loss:  0.06