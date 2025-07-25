
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

def predict(img_path='./content/cars_test/Mercedes/car__107.png', model_path='./model_avto.h5'):
    classes = {0: 'Ferrari',
               1: 'Mercedes',
               2: 'Renault',
               }

    model_conv = load_model(model_path)

    img_width, img_height = 64, 128

    img = Image.open(img_path).resize((img_height, img_width))
    image = np.array(img, dtype='float64') / 255

    image = np.expand_dims(image, axis=0)
    cls_image = np.argmax(model_conv.predict(image))

    print(classes[cls_image])
