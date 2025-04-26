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

# =================================
# Parte 2: procesamiento de datos
# ================================

from keras.preprocessing.image import ImageDataGenerator

# Generador de datos de entrenamiento con aumento (data augmentation)
# - mejora la generalizacion del modelo y evita sobreajuste

train_datagen = ImageDataGenerator(
    rescale = 1./255, # Normaliza los pixeles entre 0 y 1
    shear_range = 0.2, # Aplica transformaciones diagonales
    zoom_range = 0.2, # Aplica zoom aleatorio
    horizontal_flip = True # Invierte horizontalemnte las imagenes
)

# Generador de datos de validacion / prueba sin aumento

test_datagen = ImageDataGenerator(rescale = 1./255)

# Carga de imagenes de entrenamiento desde el directorio
# Lassubcarpetas dentro de 'training_set' deben ser cats y dogs

training_set = train_datagen.flow_from_directory(
    'dataset/training_set', # Directorio imagenes
    target_size=(64, 64), # Redimensiona las imagenes
    batch_size=32, # Numero de imagenes por lote
    class_mode = 'binary' # clasificacion binaria
)

# carga de imagenes de prueba
test_set = test_datagen.flow_from_directory(
    'dataset/training_set', # Directorio imagenes
    target_size=(64, 64), # Redimensiona las imagenes
    batch_size=32, # Numero de imagenes por lote
    class_mode = 'binary' # clasificacion binaria
)

# Entrenamiento del modelo con los datos cargados
# steps_per_epoch: numero de lotes por epoca
# epochs: numero de iteraciones completas sobre el set de entrenamiento
# validation_steps: numero de lotes de validacion por epoca

classifier.fit(
    training_set,
    steps_per_epoch=8000,
    epochs=2,
    validation_data=test_set,
    validation_steps=2000
)

# ==============================
# Parte 3: prediccion sobre nueva imagen
# ==============================

import numpy as np
from keras.preprocessing import image

# Cargar una nueva imagen para predecir
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size=(64,64))

# conversion a matriz numpy
test_image = image.img_to_array(test_image)

# Expansion de simensiones (Keras espera un lote de imagenes)
test_image = np.expand_dims(test_image, axis=0)

# Cargar una nueva imagen para predecir
test_image2 = image.load_img('dataset/single_prediction/cat_or_dog_2.jpg', target_size=(64,64))

# conversion a matriz numpy
test_image2 = image.img_to_array(test_image2)

# Expansion de simensiones (Keras espera un lote de imagenes)
test_image2 = np.expand_dims(test_image2, axis=0)

# prediccion del modelo
result = classifier.predict(test_image)
result2 = classifier.predict(test_image2)

# Diccionario de clases: {'cats': 0, 'dogs': 1}
class_names = training_set.class_indices

print("Resultado 1")
print(f"Res1 {result[0][0]}", f"Res2 {result2[0][0]}")

# Decodificacion del resultado 
prediction = 'Perro' if result[0][0] >= 0.5 else 'Gato'
prediction2 = 'Perro' if result2[0][0] >= 0.5 else 'Gato'

# Mostrar el resultado
print(f"Prediccion 1: {prediction}")
print(f"Prediccion 2: {prediction2}")