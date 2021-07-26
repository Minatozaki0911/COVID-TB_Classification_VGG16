import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from keras.models import Model, Sequential
from keras.models import load_model

IMAGE_SIZE = (224,224)
BATCH_SIZE = 32

model = load_model('~/TTTN203/SourceCode/Model/COVID_VGG16.h5', compile=True)
model.summary()

image = cv2.imread('~/TTTN203/Dataset/COVID/Covid (100).png', cv2.IMREAD_GRAYSCALE)
print(image.shape)

prediction = model.predict(image)
result = np.argmax(prediction, axis=1)
print(result)
