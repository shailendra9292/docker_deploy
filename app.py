# # Import Dependencies
# from flask import Flask, request, jsonify
# import joblib
# import traceback
# import pandas as pd
# import numpy as np

# # API definition
# app = Flask(__name__)
# @app.route('/predict', methods=['POST'])

# def predict():
#     if rf:
#         try:
#             json_ = request.json
#             print(json_)
#             query = pd.get_dummies(pd.DataFrame(json_))
#             query = query.reindex(columns=model_columns, fill_value=0)
#             print("Predicting")
#             prediction = list(rf.predict(query))
#             return jsonify({'prediction': str(prediction)})
#         except:
#             return jsonify({'trace': traceback.format_exc()})
#     else:
#         print ('Train the model first')
#         return ('No model here to use')

# if __name__ == '__main__':
#     rf = joblib.load("RandomForest.pkl") # Load "RandomForest.pkl"
#     print ('Model loaded')
#     model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
#     print ('Model columns loaded')
#     app.run(port=5000, debug=True,host='0.0.0.0')


# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model and column names
model = joblib.load("RandomForest.pkl")
model_columns = joblib.load("model_columns.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define the Pydantic model for request body
class WineData(BaseModel):
    fixed_acidity: float
    citric_acid: float
    sulphates: float
    alcohol: float

@app.post("/predict")
def predict(data: WineData):
    # Convert the request data into a DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    # Ensure the input data has the same column order as the training data
    input_data = input_data.reindex(columns=model_columns)
    
    # Make the prediction
    prediction = model.predict(input_data)
    #print(prediction)
    
    # Return the prediction result
    return {"quality": (prediction[0])}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
