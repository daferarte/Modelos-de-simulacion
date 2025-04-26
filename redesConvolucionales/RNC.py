# Creando la red neuronal convolucional
# Utilizamos keras
from keras.models import Sequential
from keras.layers import Dense

# las siguientes librerias sirven para que la red realice la convolucion, agrupamiento y aplanado
from keras.layers import Conv2D # convolucion
from keras.layers import MaxPooling2D # Agrupamiento
from keras.layers import Flatten # Aplanamiento

# inicializamos la red convolucional
classifier = Sequential()

# Capa 1: convolucion + ReLu + Maxpooling
# - 32 filtros de tamaño 3x3
# - funcion de activacion RelU
# - tamaño de entrada: 64x64 con 3 canales (RGB)
classifier.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Capa 2: Convolucion + maxpooling
# - 64 filtros
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Capa 3: Convolucion + maxpooling
# - 128 filtros para captar caracteristicas mas complejas
classifier.add(Conv2D(128, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Capa 4: Convolucion + maxpooling
# - 32 filtros para realizar caracteristicas finales
classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Capa de aplanamiento
# - Convierte los mapas de caracteristicas en un vector de 1D
classifier.add(Flatten())

# capa densa oculta
# - 128 neuronas con activacion relu

classifier.add(Dense(units=128, activacion='relu'))

# Capa de salida
# - 1 neurona con activacion sigmoide para clasificacion binaria (0 o 1)
classifier.add(Dense(units=1, activation='sigmoid'))


# Compilar el modelo
# - optimizacion con Adam
# - Funcion de perdida binaria (ideal para dos clases)
# - Metrica de evaluacion: precision
classifier.compile(optimizer='adam', loss='binary_ccrossentropy', metrics=['accuracy'])
