import json
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

print("Allo AI Neural Network Trainer")

with open("train_data.json", "r") as file:
    data = json.load(file)

patterns = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        labels.append(intent["tag"])

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(patterns)

X = tokenizer.texts_to_sequences(patterns)
X = pad_sequences(X, padding="post")

model = Sequential([
    Dense(128, activation="relu", input_shape=(X.shape[1],)),
    Dropout(0.2),
    Dense(64, activation="relu"),
    Dense(len(encoder.classes_), activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X, y, epochs=100, verbose=1)

model.save("allo_model.h5")

with open("tokenizer.pkl", "wb") as file:
    pickle.dump(tokenizer, file)

with open("labels.pkl", "wb") as file:
    pickle.dump(encoder, file)

print("Training complete!")
print("Created allo_model.h5")
