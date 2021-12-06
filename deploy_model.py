from flask import Flask, jsonify, request
import pandas as pd
from joblib import load

app = Flask(__name__)

model = load('model/model.joblib')

@app.route('/predict', methods=['POST'])
def predict(): # à modifier
 payload = request.get_json()
 input_df = pd.DataFrame(payload)
 input_df.fillna(-1, inplace=True)
 prediction = model.predict_proba(input_df)
 return jsonify({'prediction': prediction.tolist()})


# Should be called from wsgi
#if __name__ == "__main__":
# app.run(host='0.0.0.0')
