from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import keras
import cv2

app = Flask(__name__)

model = keras.models.load_model('model/resnet50')

@app.route('/predict', methods=['POST'])
def predict():
 image = request.files.get('image')
 image = cv2.resize(image, (224, 224))
 image = np.array(image)
 prediction = model.predict(image)
 return jsonify({'prediction': prediction.tolist()})


# Should be called from wsgi
#if __name__ == "__main__":
# app.run(host='0.0.0.0')
