from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input,
    Dense,
    LSTM,
    Flatten,
    Conv2D,
    MaxPooling2D,
    concatenate,
)

# Визуальный поток
visual_input = Input(shape=(48, 48, 1), name="visual_input")
x = Conv2D(32, (3, 3), activation="relu")(visual_input)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x)
visual_output = Dense(128, activation="relu")(x)

# Аудио-текстовый поток
audio_text_input = Input(shape=(100,), name="audio_text_input")
y = Dense(128, activation="relu")(audio_text_input)

# Объединение потоков
merged = concatenate([visual_output, y])
output = Dense(5, activation="linear", name="output")  # 5 выходов для OCEAN

# Финальная модель
model = Model(inputs=[visual_input, audio_text_input], outputs=output)
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

model.summary()
