
from keras.preprocessing.image import img_to_array
import numpy as np
from keras.models import load_model

fruit_names = ["Pretty", "Pretty ugly"]


def predict(image1):
    image = image1.resize((100, 100))
    image = img_to_array(image)
    image = image / 255.0

    model = load_model('second_try_food_waste_model.h5')

    prediction_image = np.expand_dims(image, axis=0)
    prediction = model.predict(prediction_image)
    value = np.argmax(prediction)
    return fruit_names[value]