# # Importar las bibliotecas necesarias
# from keras.models import Sequential
# from keras.layers import Embedding, LSTM, Dense
# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences

# # Preprocesar los datos de texto
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(texts)  # 'texts' es una lista de tus conversaciones de WhatsApp
# sequences = tokenizer.texts_to_sequences(texts)
# data = pad_sequences(sequences)

# # Crear el modelo
# model = Sequential()
# model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=128))
# model.add(LSTM(128))
# model.add(Dense(1, activation='sigmoid'))

# # Compilar el modelo
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Ajustar el modelo
# model.fit(data, labels, epochs=10, batch_size=32)  # 'labels' son las etiquetas de tus datos
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Supongamos que tienes 'texts' y 'labels' definidos

# Preprocesar los datos de texto
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
data = pad_sequences(sequences)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Crear el modelo
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=128))
model.add(LSTM(128))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Ajustar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

